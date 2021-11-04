import threading
import time
from django.contrib.postgres.fields.jsonb import KeyTextTransform
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import FloatField
from django.db.models.functions import Cast

from push_image.models import Tag


class Command(BaseCommand):

    def func1(self):
        print('--守护线程开始1--')
        check_time = time.time()
        try:
            with transaction.atomic():
                tasg = Tag.objects.select_for_update() \
                    .select_for_update().annotate(float_timestamp=Cast(KeyTextTransform(
                    'timestamp', KeyTextTransform('camera', 'data')), output_field=FloatField())).filter(
                    float_timestamp=1625720115.3385234, name=234234)
                for _ in tasg:
                    data = _.data
                    print('守护线程开始1 %s'%data)
                    if data.get('check_valid_to_push'):
                        data['check_valid_to_push'].append({
                            'caller_name': 'func2',

                            'check_time': check_time
                        })
                    else:
                        data['check_valid_to_push'] = [{
                            'caller_name': 'func2',

                            'check_time': check_time
                        }]

                    _.data = data
                    _.save(update_fields=['data', ])
                time.sleep(5)
        except Exception as e:
            print(e)
        print('--守护线程结束1--')

    def func2(self):
        print('--守护线程开始2--')
        check_time = time.time()
        try:
            with transaction.atomic():
                tasg = Tag.objects \
                    .annotate(float_timestamp=Cast(KeyTextTransform(
                    'timestamp', KeyTextTransform('camera', 'data')), output_field=FloatField())).filter(
                    float_timestamp=1625720115.3385234, name=234234)

                for _ in tasg:
                    print(tasg.query)
                    data = _.data
                    print('非守护线程开始2 %s' % data)
                    if data.get('check_valid_to_push'):
                        data['check_valid_to_push'].append({
                            'caller_name': 'func2',

                            'check_time': check_time
                        })
                    else:
                        data['check_valid_to_push'] = [{
                            'caller_name': 'func2',

                            'check_time': check_time
                        }]

                    _.data = data
                    _.save(update_fields=['data', ])
                    time.sleep(2)
        except Exception as e:
            print(e)
        print('--守护线程结束2--')

    def handle(self, *args, **options):
        index =1
        while True:
            print('第%s并发' % index)
            tag=Tag.objects.filter(name=234234).first()
            if tag.data and tag.data.get('check_valid_to_push') and  len(tag.data.get('check_valid_to_push'))==1:
                return
            Tag.objects.filter(name=234234).update(data={"camera": {"timestamp": "1625720115.3385234"}, "check_valid_to_push": []})
            t1 = threading.Thread(target=self.func1, args=())
            t2 = threading.Thread(target=self.func2, args=())
            t1.start()

            t2.start()
            t1.join()
            t2.join()
            index+=1
            time.sleep(20)

