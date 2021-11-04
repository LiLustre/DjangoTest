import threading
import time
from django.contrib.postgres.fields.jsonb import KeyTextTransform
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import FloatField
from django.db.models.functions import Cast

from push_image.models import Tag


class Command(BaseCommand):



    def handle(self, *args, **options):
        index =1

        tag1 = Tag()
        tag1.name='aaaa'
        tag =Tag()
        #tag.id= 3
        tag.name='注：序号、分类与车位编号为必填项，注：序号、分类与车位编号为必填项，分类与车位编号为必填项分类与车位编号为必填项分类与车位编号为必填项分类与车位编号为必填项分类与车位编号为必填项注：序号、分类与车位编号为必填项，注：序号、分类与车位编号为必填项，注：序号、分类与车位编号为必填项，注：序号、分类与车位编号为必填项，'
        #Tag.objects.bulk_update([tag],['name'])
        Tag.objects.bulk_create([tag1,tag],batch_size=1)




