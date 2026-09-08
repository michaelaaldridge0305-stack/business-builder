import unittest
from unittest.mock import patch

import watch_video


class YouTubeClipTests(unittest.TestCase):
    @patch.object(watch_video, "json_request")
    def test_clip_and_fps_use_video_metadata(self, request):
        request.return_value = (
            {"candidates": [{"content": {"parts": [{"text": "Analysis complete"}]}}]},
            {},
        )

        result = watch_video.analyze_video(
            "https://www.youtube.com/watch?v=example",
            prompt="Analyze the hook",
            clip="0:00-0:05",
            fps=10,
            key="test-key",
        )

        self.assertEqual(result, "Analysis complete")
        payload = request.call_args.kwargs["payload"]
        video_part = payload["contents"][0]["parts"][0]
        self.assertEqual(
            video_part["videoMetadata"],
            {"startOffset": "0.0s", "endOffset": "5.0s", "fps": 10},
        )
        self.assertIn(":generateContent", request.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
