import random
import time
import requests
from django.core.management.base import BaseCommand
from requests_toolbelt import MultipartEncoder


class Command(BaseCommand):
    def handle(self, *args, **options):
        for index in range(10000000):
           # with open('imags/15_56_52.jpg', 'rb') as _file:
            with open('imags/wt.jpg', 'rb') as _file:
                content = _file.read()
                _len = len(content)
                # print(type(content))
                # print(content)
                chunk_length = int(_len / 2)
                print(chunk_length)
                m = MultipartEncoder(
                    fields={
                        'dev_id': '202111040033001',
                        'timestamp': str(time.time()),
                        'cam_id':'1',
                        'chunks': '1',
                        'chunk': '1',
                        'upload': ('%s_%s.jpg' % ('11361', 'tst'), content, 'image/jpeg')
                    },
                    boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))
                )
                resp = requests.post(
                    url='https://camera-monitor-server.parkone.cn/v3/dev/upload',
                    headers={'Content-Type': m.content_type},
                    data=m,
                    timeout=10,
                )

                print(resp.status_code)
                time.sleep(40)


