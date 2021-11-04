import json
import time
import requests
from django.core.management.base import BaseCommand
from google.protobuf.json_format import MessageToJson

from push_image import msg_pb2


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                resp = requests.get(
                   # url='http://192.168.6.75:8000/v3/dev/cmd',
                    url='http://camera-monitor-deployment-server.parkone.cn/v3/dev/cmd',
                    params={
                        'dev_id':'862167058979570',
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


