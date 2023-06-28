import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')

class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel_id = channel_id
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']["thumbnails"]["default"]["url"]
        self.subscriber_count = channel['items'][0]["statistics"]['subscriberCount']
        self.video_count = channel['items'][0]["statistics"]['videoCount']
        self.view_count = channel['items'][0]["statistics"]['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_to_print = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename):
        with open(filename, 'w') as file:
            file.write(json.dumps({
                "channel_id": self.channel_id,
                "title": self.title,
                "description": self.description,
                "subscriber_count": self.subscriber_count,
                "video_count": self.video_count,
                "view_count": self.view_count
            }, indent=2, ensure_ascii=False))
