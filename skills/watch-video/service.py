"""Secure ChatGPT Action service for the watch-video skill."""

from __future__ import annotations

import ipaddress
import os
import socket
import sqlite3
import tempfile
import threading
import urllib.parse
import urllib.request
import uuid
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from pathlib import Path
from typing import Literal

from fastapi import BackgroundTasks, Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field, model_validator

from watch_video import DEFAULT_PROMPT, analyze_video, is_youtube

APP_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.getenv("WATCH_VIDEO_DB", str(APP_DIR / "watch-video-jobs.sqlite3")))
MAX_UPLOAD_BYTES = int(os.getenv("MAX_UPLOAD_BYTES", str(512 * 1024 * 1024)))
ALLOWED_VIDEO_SUFFIXES = {".mp4", ".mov", ".mpeg", ".mpg", ".avi", ".webm", ".flv", ".wmv", ".3gp", ".3gpp"}
executor = ThreadPoolExecutor(max_workers=int(os.getenv("WATCH_VIDEO_WORKERS", "2")))
db_lock = threading.Lock()
public_base_url = os.getenv("PUBLIC_BASE_URL") or os.getenv("RENDER_EXTERNAL_URL")

app = FastAPI(
    title="Ikhaya Watch Video",
    version="1.0.0",
    description="Analyze public YouTube URLs or videos uploaded to ChatGPT with Gemini.",
    servers=[{"url": public_base_url.rstrip("/")}] if public_base_url else None,
)


class OpenAIFileRef(BaseModel):
    name: str
    id: str | None = None
    mime_type: str | None = Field(default=None, alias="mime_type")
    download_link: str


class AnalysisRequest(BaseModel):
    youtube_url: str | None = None
    openaiFileIdRefs: list[OpenAIFileRef] | None = None
    clip: str | None = Field(default=None, examples=["0:00-0:05"])
    fps: float | None = Field(default=None, gt=0, le=24)
    prompt: str | None = Field(default=None, max_length=12000)

    @model_validator(mode="after")
    def exactly_one_source(self):
        file_count = len(self.openaiFileIdRefs or [])
        if bool(self.youtube_url) == bool(file_count):
            raise ValueError("Provide exactly one YouTube URL or one uploaded video.")
        if file_count > 1:
            raise ValueError("Upload one video per analysis.")
        if self.youtube_url and not is_youtube(self.youtube_url):
            raise ValueError("youtube_url must be a public youtube.com or youtu.be URL.")
        return self


class JobResponse(BaseModel):
    job_id: str
    status: Literal["queued", "running", "complete", "failed"]
    analysis: str | None = None
    error: str | None = None


def require_action_key(x_action_key: str = Header(default="")) -> None:
    expected = os.getenv("ACTION_API_KEY", "")
    if not expected or not __import__("hmac").compare_digest(x_action_key, expected):
        raise HTTPException(status_code=401, detail="Invalid action key")


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(DB_PATH)) as db:
        db.execute(
            "CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, status TEXT NOT NULL, "
            "analysis TEXT, error TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)"
        )
        db.commit()


def update_job(job_id: str, status: str, *, analysis: str | None = None, error: str | None = None) -> None:
    with db_lock, closing(sqlite3.connect(DB_PATH)) as db:
        db.execute(
            "UPDATE jobs SET status = ?, analysis = ?, error = ? WHERE id = ?",
            (status, analysis, error, job_id),
        )
        db.commit()


def validate_public_https(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("Uploaded-file link must use HTTPS.")
    for record in socket.getaddrinfo(parsed.hostname, parsed.port or 443, type=socket.SOCK_STREAM):
        address = ipaddress.ip_address(record[4][0])
        if not address.is_global:
            raise ValueError("Uploaded-file link resolved to a non-public address.")


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_public_https(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def download_upload(ref: OpenAIFileRef, target_dir: Path) -> Path:
    validate_public_https(ref.download_link)
    suffix = Path(ref.name).suffix.lower()
    if suffix not in ALLOWED_VIDEO_SUFFIXES:
        raise ValueError(f"Unsupported uploaded video format: {suffix or '(none)'}")
    target = target_dir / f"input{suffix}"
    request = urllib.request.Request(ref.download_link, headers={"User-Agent": "ikhaya-watch-video/1.0"})
    opener = urllib.request.build_opener(SafeRedirectHandler())
    total = 0
    with opener.open(request, timeout=120) as response, target.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            total += len(chunk)
            if total > MAX_UPLOAD_BYTES:
                raise ValueError("Uploaded video exceeds the configured size limit.")
            output.write(chunk)
    return target


def run_job(job_id: str, request: AnalysisRequest) -> None:
    update_job(job_id, "running")
    try:
        with tempfile.TemporaryDirectory(prefix="watch-video-") as temp:
            source = request.youtube_url
            if request.openaiFileIdRefs:
                source = str(download_upload(request.openaiFileIdRefs[0], Path(temp)))
            result = analyze_video(
                source or "",
                prompt=request.prompt or DEFAULT_PROMPT,
                clip=request.clip,
                fps=request.fps,
            )
        update_job(job_id, "complete", analysis=result)
    except (Exception, SystemExit) as exc:
        update_job(job_id, "failed", error=str(exc)[:2000])


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health", include_in_schema=False)
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/v1/analyses",
    response_model=JobResponse,
    dependencies=[Depends(require_action_key)],
    operation_id="create_analysis",
)
def create_analysis(request: AnalysisRequest, background_tasks: BackgroundTasks) -> JobResponse:
    job_id = uuid.uuid4().hex
    with db_lock, closing(sqlite3.connect(DB_PATH)) as db:
        db.execute("INSERT INTO jobs (id, status) VALUES (?, 'queued')", (job_id,))
        db.commit()
    background_tasks.add_task(executor.submit, run_job, job_id, request)
    return JobResponse(job_id=job_id, status="queued")


@app.get(
    "/v1/analyses/{job_id}",
    response_model=JobResponse,
    dependencies=[Depends(require_action_key)],
    operation_id="get_analysis",
)
def get_analysis(job_id: str) -> JobResponse:
    with closing(sqlite3.connect(DB_PATH)) as db:
        row = db.execute("SELECT status, analysis, error FROM jobs WHERE id = ?", (job_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Analysis job not found")
    return JobResponse(job_id=job_id, status=row[0], analysis=row[1], error=row[2])
