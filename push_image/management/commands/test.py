import json
import random
import time
import requests
from django.core.management.base import BaseCommand
from google.protobuf.json_format import MessageToJson
from requests_toolbelt import MultipartEncoder

from push_image.management import msg_pb2
from push_image.models import Article, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Article.objects.create(**{
        #     'name':'111233'
        # })
        # Tag.objects.create(**{
        #     'name': 'ttttt2'
        # })
        art =Article.objects.get(name='111233')
        art.tags.add(
            Tag.objects.get(name='ttttt2')
        )
                #time.sleep(1)


