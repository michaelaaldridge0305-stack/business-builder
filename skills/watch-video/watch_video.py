#!/usr/bin/env python3
"""Analyze a YouTube URL or local video with Gemini's Interactions API.

Usage:
  python watch_video.py SOURCE [--clip 0:00-0:05] [--fps 10] [--prompt "..."]

Environment:
  GEMINI_API_KEY  Required.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

API_ROOT = "https://generativelanguage.googleapis.com"
INTERACTIONS_URL = f"{API_ROOT}/v1beta/interactions"
FILES_URL = f"{API_ROOT}/upload/v1beta/files"
DEFAULT_MODEL = "gemini-3.8-flash"
INLINE_LIMIT = 95 * 1024 * 1024
POLL_SECONDS = 3
PROCESSING_TIMEOUT = 300

VIDEO_MIME = {
    ".mp4": "video/mp4",
    ".mov": "video/mov",
    ".mpeg": "video/mpeg",
    ".mpg": "video/mpg",
    ".avi": "video/avi",
    ".webm": "video/webm",
    ".flv": "video/x-flv",
    ".wmv": "video/wmv",
    ".3gp": "video/3gpp",
    ".3gpp": "video/3gpp",
}

DEFAULT_PROMPT = """Analyze the supplied video carefully. Ground every claim in what is
actually visible or audible. If something is uncertain, say so.

Return markdown with these sections:

## Summary
A concise account of what happens and the apparent purpose/audience.

## Scene-by-scene
Use the video's own timestamps. For each meaningful beat, record:
- what is visible
- what is said or heard
- exact on-screen wording when legible
- the transition/cut when relevant

## Audio
Describe speech, music and sound effects. If there is no speech, state that plainly.

## On-screen text and visual treatment
List important text overlays/captions with timestamps, plus placement, hierarchy,
typography/visual style, branding and product visibility.

## Structure
Identify the hook, tension/turn, payoff and close/CTA, with timestamps where supported.

## Pacing and edit
Describe cut frequency, rhythm, changes in pace, b-roll, camera movement and transitions.
Do not claim a precise average cut length unless you can support it from the video.

## Key moments
List the most memorable moments with supported timestamps.

## Marketing/creative lessons
Explain why the presentation may work, separating observation from interpretation.
Extract reusable principles rather than copying wording, graphics or creator identity.

## Ikhaya application
When relevant, translate those principles into practical ideas for Ikhaya Designs or
Ikhaya Automations, especially Etsy listing images, hero thumbnails, Pinterest pins,
Instagram/Reels, product proof, mobile readability and crop-safe composition.
"""


def fail(message: str, hint: str | None = None) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    if hint:
        print(hint, file=sys.stderr)
    raise SystemExit(1)


def info(message: str) -> None:
    print(f"[watch-video] {message}", file=sys.stderr)


def api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        fail(
            "GEMINI_API_KEY is not set.",
            "Create a key in Google AI Studio and set it in your terminal environment.",
        )
    return key


def is_youtube(source: str) -> bool:
    return bool(
        re.match(
            r"^https?://(?:(?:www|m)\.)?(?:youtube\.com|youtu\.be)/",
            source.strip(),
            flags=re.IGNORECASE,
        )
    )


def stamp_to_seconds(value: str) -> float:
    value = value.strip()
    if not value:
        fail("Empty timestamp in --clip.")
    try:
        parts = [float(p) for p in value.split(":")]
    except ValueError:
        fail(f"Cannot parse timestamp '{value}'. Use forms such as 0:05 or 1:02:30.")
    if len(parts) > 3:
        fail(f"Cannot parse timestamp '{value}'. Use forms such as 0:05 or 1:02:30.")
    total = 0.0
    for part in parts:
        total = total * 60 + part
    return total


def parse_clip(value: str | None) -> tuple[float, float] | None:
    if not value:
        return None
    if "-" not in value:
        fail("--clip needs a start and end, for example 0:00-0:05.")
    start_text, end_text = value.split("-", 1)
    start, end = stamp_to_seconds(start_text), stamp_to_seconds(end_text)
    if end <= start:
        fail("--clip end must be after its start.")
    return start, end


def json_request(
    url: str,
    *,
    key: str,
    payload: dict[str, Any] | None = None,
    raw: bytes | None = None,
    extra_headers: dict[str, str] | None = None,
    timeout: int = 600,
) -> tuple[dict[str, Any], dict[str, str]]:
    data = raw
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(url, data=data, method="POST" if data is not None else "GET")
    request.add_header("x-goog-api-key", key)
    if payload is not None:
        request.add_header("Content-Type", "application/json")
    for name, value in (extra_headers or {}).items():
        request.add_header(name, value)

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
            parsed = json.loads(body) if body else {}
            return parsed, {k.lower(): v for k, v in response.headers.items()}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:1200]
        try:
            detail = json.loads(detail).get("error", {}).get("message", detail)
        except json.JSONDecodeError:
            pass
        if exc.code == 401 or "API key not valid" in detail:
            fail("Gemini rejected the API key.", "Create a fresh key in Google AI Studio.")
        if exc.code == 429:
            fail("Gemini rate limit reached.", "Retry later or analyze a shorter clip.")
        if exc.code == 404:
            fail(f"Gemini endpoint/model was not found: {detail}", "Try --model gemini-3.7-flash.")
        fail(f"Gemini API returned HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        fail(f"Could not reach Gemini API: {exc.reason}")


def mime_for(path: Path) -> str:
    known = VIDEO_MIME.get(path.suffix.lower())
    if known:
        return known
    guessed, _ = mimetypes.guess_type(path.name)
    if guessed and guessed.startswith("video/"):
        return guessed
    fail(
        f"Unsupported video format '{path.suffix or '(none)'}'.",
        "Re-export the video as MP4, MOV, MPEG, AVI, WebM, FLV, WMV or 3GP.",
    )


def upload_video(path: Path, key: str, mime: str) -> tuple[str, str]:
    size = path.stat().st_size
    info(f"Uploading {path.name} ({size / 1024 / 1024:.1f} MB) to Gemini Files API.")

    _, headers = json_request(
        FILES_URL,
        key=key,
        payload={"file": {"display_name": path.name}},
        extra_headers={
            "X-Goog-Upload-Protocol": "resumable",
            "X-Goog-Upload-Command": "start",
            "X-Goog-Upload-Header-Content-Length": str(size),
            "X-Goog-Upload-Header-Content-Type": mime,
        },
    )
    upload_url = headers.get("x-goog-upload-url")
    if not upload_url:
        fail("Gemini did not return an upload URL.")

    result, _ = json_request(
        upload_url,
        key=key,
        raw=path.read_bytes(),
        extra_headers={
            "Content-Length": str(size),
            "Content-Type": mime,
            "X-Goog-Upload-Offset": "0",
            "X-Goog-Upload-Command": "upload, finalize",
        },
    )
    file_info = result.get("file", {})
    name = file_info.get("name")
    uri = file_info.get("uri")
    if not name or not uri:
        fail("Gemini upload completed without a usable file reference.")

    deadline = time.time() + PROCESSING_TIMEOUT
    while time.time() < deadline:
        state = str(file_info.get("state", "")).upper()
        if state == "ACTIVE":
            return uri, file_info.get("mimeType") or file_info.get("mime_type") or mime
        if state == "FAILED":
            fail("Gemini could not process the uploaded video.", "Try re-exporting it as MP4.")
        time.sleep(POLL_SECONDS)
        file_info, _ = json_request(f"{API_ROOT}/v1beta/{name}", key=key)

    fail("Gemini is still processing the upload after five minutes.", "Try a shorter video.")


def video_input(source: str, key: str) -> dict[str, Any]:
    if is_youtube(source):
        info("Using the public YouTube URL directly.")
        return {"type": "video", "uri": source}

    path = Path(source).expanduser().resolve()
    if not path.is_file():
        fail(f"No video file found at {path}")
    mime = mime_for(path)

    if path.stat().st_size < INLINE_LIMIT:
        info(f"Sending local video inline ({path.stat().st_size / 1024 / 1024:.1f} MB).")
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        return {"type": "video", "data": encoded, "mime_type": mime}

    uri, uploaded_mime = upload_video(path, key, mime)
    return {"type": "video", "uri": uri, "mime_type": uploaded_mime}


def analyze_video(
    source: str,
    *,
    prompt: str = DEFAULT_PROMPT,
    clip: str | None = None,
    fps: float | None = None,
    model: str = DEFAULT_MODEL,
    key: str | None = None,
) -> str:
    """Analyze a source and return markdown; shared by the CLI and web service."""
    resolved_key = key or api_key()
    parsed_clip = parse_clip(clip)
    if is_youtube(source) and (parsed_clip or fps is not None):
        return analyze_youtube_clip(
            source,
            prompt=prompt,
            clip=parsed_clip,
            fps=fps,
            model=model,
            key=resolved_key,
        )
    video = video_input(source, resolved_key)
    add_processing(video, parsed_clip, fps)
    payload = {
        "model": model,
        "input": [video, {"type": "text", "text": prompt}],
    }
    info(f"Analyzing with {model}.")
    response, _ = json_request(INTERACTIONS_URL, key=resolved_key, payload=payload)
    return extract_text(response)


def add_processing(video: dict[str, Any], clip: tuple[float, float] | None, fps: float | None) -> None:
    if fps is not None and not (0 < fps <= 24):
        fail("--fps must be greater than 0 and no more than 24.")

    if not clip and fps is None:
        return

    processing: dict[str, Any] = {"type": "static"}
    if clip:
        processing["start_offset"], processing["end_offset"] = clip
    if fps is not None:
        processing["fps"] = fps
    video["processing"] = processing


def extract_text(response: dict[str, Any]) -> str:
    chunks: list[str] = []
    for step in response.get("steps", []):
        if step.get("type") != "model_output":
            continue
        for block in step.get("content", []):
            if block.get("type") == "text" and block.get("text"):
                chunks.append(block["text"])
    if chunks:
        return "\n".join(chunks).strip()

    for key in ("output_text", "text"):
        if isinstance(response.get(key), str) and response[key].strip():
            return response[key].strip()
    fail(f"Unexpected Gemini response shape: {json.dumps(response)[:800]}")


def extract_generate_content_text(response: dict[str, Any]) -> str:
    chunks: list[str] = []
    for candidate in response.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if isinstance(part.get("text"), str):
                chunks.append(part["text"])
    if chunks:
        return "\n".join(chunks).strip()
    fail(f"Unexpected Gemini response shape: {json.dumps(response)[:800]}")


def analyze_youtube_clip(
    source: str,
    *,
    prompt: str,
    clip: tuple[float, float] | None,
    fps: float | None,
    model: str,
    key: str,
) -> str:
    """Use GenerateContent videoMetadata for YouTube clipping/custom FPS."""
    metadata: dict[str, Any] = {}
    if clip:
        metadata["startOffset"] = f"{clip[0]}s"
        metadata["endOffset"] = f"{clip[1]}s"
    if fps is not None:
        metadata["fps"] = fps
    part: dict[str, Any] = {"fileData": {"fileUri": source, "mimeType": "video/*"}}
    if metadata:
        part["videoMetadata"] = metadata
    payload = {
        "contents": [{"role": "user", "parts": [part, {"text": prompt}]}],
    }
    url = f"{API_ROOT}/v1beta/models/{urllib.parse.quote(model, safe='')}:generateContent"
    info(f"Analyzing YouTube clip with {model} video metadata.")
    response, _ = json_request(url, key=key, payload=payload)
    return extract_generate_content_text(response)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze real video frames and audio with Gemini.")
    parser.add_argument("source", help="Public YouTube URL or local video file path")
    parser.add_argument("--clip", help="Optional range such as 0:00-0:05")
    parser.add_argument("--fps", type=float, help="Static frame sampling rate; use 6-10 for short fast-cut clips")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="Question/instructions for Gemini")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini model (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    print(
        analyze_video(
            args.source,
            prompt=args.prompt,
            clip=args.clip,
            fps=args.fps,
            model=args.model,
        )
    )


if __name__ == "__main__":
    main()
