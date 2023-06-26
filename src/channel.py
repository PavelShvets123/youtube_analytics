import json
import os
from googleapiclient.discovery import build

from helper.youtube_api_manual import channel_id, api_key

youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        # self.data_id = channel_id['items']['snipped']['title']
        self.title = channel_id['items'][0]['snipped']['title']
        # self.description = description
        # self.subscriber_count = subscriber_count
        # self.video_count = video_count
        # self.view_count = view_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_to_print = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, dict_to_print):
        json.dumps(dict_to_print, indent=2, ensure_ascii=False)
