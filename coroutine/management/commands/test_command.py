import random
import time
import requests
from django.core.management.base import BaseCommand
from requests_toolbelt import MultipartEncoder


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('test_command.py start'))
        time.sleep(10)
        self.stdout.write(self.style.SUCCESS('test_command.py ok'))
