from urllib import request
from xml.etree import ElementTree

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ytindex.indexing import Index
from ytindex.indexing.ytapi import Youtube
from ytindex.indexing.downloader import YTCaptionDownloader, YTCaptionNotFoundException

class Command(BaseCommand):
    help = 'Index the latest videos from a channel'

    def add_arguments(self, parser):
        parser.add_argument('index', type=str)
        parser.add_argument('playlist_ids', nargs='+', type=str)

    def handle(self, *args, **options):

        index = options['index']

        def index_video(ytid, idx):
            downloader = YTCaptionDownloader(ytid)
            idx.index_object(downloader.as_dict())

        for playlist_id in options['playlist_ids']:
            idx = Index(**settings.YTCI_SETTINGS[index]['elastic'])
            y = Youtube( settings.YTCI_SETTINGS['api_key'] )
            for video_id in y.listplaylist(playlist_id):
                try:
                    print('Indexing::', video_id)
                    index_video(video_id, idx)
                except YTCaptionNotFoundException as e:
                    print(e)
                except Exception as e:
                    print('Most unexpected!!!', e)
