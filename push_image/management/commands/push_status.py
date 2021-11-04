import random
import time

#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         while True:
#             i = 0
#             for _ in ['862167057472734','862167058968458','1451651616','888888888888881']:
#                 i+=1
#                 try:
#                     status = msg_pb2.Status()
#                     status.dev_id=_
#                     status.version='v1.5.2-beta.1'
#                     status.timestamp=int(time.time())
#                     status.vbat=random.uniform(2,4.54)
#                     status.rssi='-63dbm'
#                     status.iccid='1231231231231'+str(i)
#                     resp = requests.post(
#                        # url='http://192.168.6.75:8000/v3/dev/cmd',
#                         url='http://camera-monitor-deployment-server-d.parkone.cn/v3/dev/status',
#                         data= status.SerializeToString(),
#                         timeout=10,
#                     )
#                     if resp :
#                         print(resp.status_code)
#                 except Exception as e:
#                         print(e)
#             time.sleep(120)
#                 #time.sleep(1)
#
#
from push_image import msg_pb2

status = msg_pb2.Status()
status.dev_id='1111'
status.version='v1.5.2-beta.1'
status.timestamp=int(time.time())
status.vbat=random.uniform(2,4.54)
status.rssi='-63dbm'
status.iccid='1231231231231'
print( status.SerializeToString())