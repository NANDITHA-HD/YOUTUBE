from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

class YouTubeTranscriptAPI:
    def __init__(self):
        pass

    def fetch_transcript(self, video_id, languages=['en']):
        """Fetch the transcript of a given video."""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            return transcript
        except NoTranscriptFound:
            return None

    def fetch_transcript_translated(self, video_id, target_language='en'):
        """Fetch and translate the transcript of a video."""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            translated_transcript = YouTubeTranscriptApi.translate_transcript(transcript, target_language)
            return translated_transcript
        except NoTranscriptFound:
            return None
