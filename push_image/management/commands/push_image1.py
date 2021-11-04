import base64
import json
import random
import time
import requests
from django.core.management.base import BaseCommand
from requests_toolbelt import MultipartEncoder


class Command(BaseCommand):
    def handle(self, *args, **options):
        # with open('imags/15_56_52.jpg', 'rb') as _file:
        m = MultipartEncoder(
            fields={
                'dev_id': 'DD11111111111',
                'timestamp': str(time.time()),
                'cam_id': '1',
                'chunks': '1',
                'chunk': '1',
                'upload': ('%s_%s.jpg' % ('11361', 'tst'), open('imags/dd.jpg', 'rb').read(), 'image/jpeg')
            },

        )
        resp = requests.post(
            url='http://192.168.6.75:8001/api/platenumber/identification',
            data = {'device_id': 'DD11111111111',
                    'collection_type': '1',
                    'chunks': '1',
                    'chunk': '1',},
            files={'image': open('imags/dd.jpg', 'rb'),
                   },
            timeout=10,
        )
