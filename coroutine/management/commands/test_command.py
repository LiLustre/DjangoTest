import random
import time
import requests
from django.core.management.base import BaseCommand
from requests_toolbelt import MultipartEncoder

from coroutine.models import CameraInfo, Spot


class Command(BaseCommand):
    def handle(self, *args, **options):
       # camerainf = CameraInfo()
       # camerainf.remark='test1'
       # camerainf.save()
       # spot1 = Spot()
       # spot1.spot_id=1
       # spot1.spot_num = '111'
       # spot2 = Spot()
       # spot2.spot_id = 2
       # spot2.spot_num = '222'
       # spot1.save()
       # spot2.save()

       camera = CameraInfo.objects.filter(camera_info_id='1').first()
       spot= Spot.objects.filter(spot_id='1').first()
       print(camera)
       print(spot)
       camera.spots.add(spot)