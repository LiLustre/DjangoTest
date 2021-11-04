import base64
import json
import random
import time
import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from requests_toolbelt import MultipartEncoder

from push_image.models import Teacher, Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            for stu in Student.objects.all():
                teacher_dict={}
                for _ in stu.teachers.all().order_by('id'):
                    teacher_dict[_.teacher_name]=_
                for key in teacher_dict:
                    teacher= teacher_dict[key]
                    teacher.teacher_name=teacher.teacher_name+'_test'
                    teacher.save()

                for teacher1 in stu.teachers.all():
                    print(teacher1.teacher_name)
