
### Step 3: Implement Modules

#### `youtube_data.py`


from googleapiclient.discovery import build

class YouTubeDataAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_details(self, video_id):
        """Retrieve video details such as title, description, view count, like count."""
        request = self.youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        )
        response = request.execute()
        return response

    def search_videos(self, query, max_results=5):
        """Search for videos based on keywords."""
        request = self.youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        return response

    def list_channel_videos(self, channel_id, max_results=5):
        """List videos from a specific channel."""
        request = self.youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=max_results,
            order='date'
        )
        response = request.execute()
        return response
