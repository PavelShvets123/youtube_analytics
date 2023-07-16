import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:

    def __init__(self, video_id):
        try:
            self.__video_id__ = video_id
            dict_to_print = youtube.videos().list(id=self.__video_id__, part='snippet,statistics').execute()
            self.title = dict_to_print['items'][0]['snippet']['title']
            self.url = f'https://youtu.be/{dict_to_print["etag"]}'
            self.view_count = dict_to_print['items'][0]['statistics']['viewCount']
            self.like_count = dict_to_print['items'][0]['statistics']['likeCount']
        except IndexError:
            self.__video_id__ = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id
