import unittest
from youtube_api.youtube_transcript import YouTubeTranscriptAPI

class TestYouTubeTranscriptAPI(unittest.TestCase):
    def setUp(self):
        self.youtube_transcript = YouTubeTranscriptAPI()

    def test_fetch_transcript(self):
        video_id = 'VIDEO_ID'  # Replace with a test video ID
        transcript = self.youtube_transcript.fetch_transcript(video_id)
        self.assertIsNotNone(transcript)

    def test_fetch_transcript_translated(self):
        video_id = 'VIDEO_ID'  # Replace with a test video ID
        transcript = self.youtube_transcript.fetch_transcript_translated(video_id, target_language='es')
        self.assertIsNotNone(transcript)

if __name__ == '__main__':
    unittest.main()
