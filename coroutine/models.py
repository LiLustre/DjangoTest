import uuid

from django.contrib.auth.models import Permission
from django.db import models

class Spot(models.Model):
    # 主键
    spot_id = models.CharField(max_length=32, primary_key=True,)


    # 泊位编号
    spot_num = models.CharField(max_length=100, db_index=True)


    class Meta:
        db_table = 'spot'

#
class CamerasSpots(models.Model):
    camera_info = models.ForeignKey('coroutine.CameraInfo', on_delete=models.CASCADE)
    spot = models.ForeignKey('coroutine.Spot', on_delete=models.CASCADE)

    sort = models.IntegerField(default=0, null=True)
    remark = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'camera_info_spots'


class CameraInfo(models.Model):


    # 相机主键id
    camera_info_id = models.CharField(max_length=32, primary_key=True,)
    # 设备和泊位多对多
    spots = models.ManyToManyField(Spot, related_name='camera_infos', null=True,through=CamerasSpots)
    #spots = models.ManyToManyField(Spot, related_name='camera_infos', null=True)
   # camera_spots = models.ManyToManyField(Spot, related_name='cameras', null=True, through=CamerasSpots)
    remark = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'camera_info'



