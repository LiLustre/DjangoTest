import base64
import json
import random
import time
import requests
from django.core.management.base import BaseCommand
from requests_toolbelt import MultipartEncoder

from push_image.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        tag = Tag()
        name = '11'
        for _ in range(98):
            name=name+'你'
        print(len(name))
        tag.name=name
        tag.save()
