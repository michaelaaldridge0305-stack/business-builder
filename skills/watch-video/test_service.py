import os
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("ACTION_API_KEY", "test-action-key")
os.environ.setdefault("GEMINI_API_KEY", "test-gemini-key")
os.environ.setdefault("PUBLIC_BASE_URL", "https://video-analyser.example.com")

import service


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        service.DB_PATH = Path(self.temp.name) / "jobs.sqlite3"
        service.init_db()

    def tearDown(self):
        self.temp.cleanup()

    def test_rejects_non_youtube_url(self):
        with self.assertRaises(ValueError):
            service.AnalysisRequest(youtube_url="https://example.com/video.mp4")

    def test_requires_one_source(self):
        with self.assertRaises(ValueError):
            service.AnalysisRequest()

    def test_openapi_declares_public_server(self):
        self.assertEqual(
            service.app.openapi()["servers"],
            [{"url": "https://video-analyser.example.com"}],
        )

    @patch.object(service, "analyze_video", return_value="# Analysis\nDone")
    def test_youtube_job_completes(self, mocked):
        job_id = "abc123"
        with closing(service.sqlite3.connect(service.DB_PATH)) as db:
            db.execute("INSERT INTO jobs (id, status) VALUES (?, 'queued')", (job_id,))
            db.commit()
        request = service.AnalysisRequest(youtube_url="https://youtu.be/example")
        service.run_job(job_id, request)
        with closing(service.sqlite3.connect(service.DB_PATH)) as db:
            row = db.execute("SELECT status, analysis FROM jobs WHERE id = ?", (job_id,)).fetchone()
        self.assertEqual(row, ("complete", "# Analysis\nDone"))
        mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()
