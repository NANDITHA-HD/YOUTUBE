import unittest
from youtube_api.youtube_data import YouTubeDataAPI

class TestYouTubeDataAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'YOUR_API_KEY'  # Replace with your API key for testing
        self.youtube_data = YouTubeDataAPI(self.api_key)

    def test_get_video_details(self):
        video_id = 'VIDEO_ID'  # Replace with a test video ID
        response = self.youtube_data.get_video_details(video_id)
        self.assertIn('items', response)

    def test_search_videos(self):
        query = 'test'
        response = self.youtube_data.search_videos(query)
        self.assertIn('items', response)

    def test_list_channel_videos(self):
        channel_id = 'CHANNEL_ID'  # Replace with a test channel ID
        response = self.youtube_data.list_channel_videos(channel_id)
        self.assertIn('items', response)

if __name__ == '__main__':
    unittest.main()
