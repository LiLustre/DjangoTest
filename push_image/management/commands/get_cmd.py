import json
import random
import time
import requests
from django.core.management.base import BaseCommand
from google.protobuf.json_format import MessageToJson
from requests_toolbelt import MultipartEncoder

from push_image.management import msg_pb2


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                resp = requests.get(
                    url='https://camera-monitor-deployment-server-d.parkone.cn/v3/dev/cmd',
                    params={
                        'dev_id':'888888888888881',
                        'last_modified':1
                    },
                    timeout=10,
                )
                if resp and resp.content :
                    print(resp.status_code)
                    print(resp.content)
                    status_decode = msg_pb2.Actions()
                    status_decode.ParseFromString(resp.content)
                    json_data = json.loads(MessageToJson(status_decode, preserving_proto_field_name=True))  # 转成json字典
                    print(json_data)
            except Exception as e:
                    print(e)
            time.sleep(5)
                #time.sleep(1)


