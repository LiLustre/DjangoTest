import os
import random
import time

import gevent
from django.core.management import BaseCommand

from gevent import monkey
monkey.patch_all(thread=False)


class Command(BaseCommand):

    def work1(self,num):
        print("正在执行work1（）" + str(num))
        print(time.time())
        # time.sleep(0.5)#模拟阻塞        默认情况下，time.sleep不能够被gevent识别为耗时操作，因此可以用gevent.sleep
        # gevent.sleep(0.5)
        #      但是就是想用time.sleep，需要进行下面操作
        #         进行打补丁
        #         1.导入monkey模块
        #         2.破解  monkey.patch_all()
        time.sleep(random.randint(0, 5))
        print("执行完毕 " + str(num))


    def work2(self,num):
        print("正在执行work2（）" + str(num))
        print(time.time())
        os.system('python manage.py test_command')
        print("执行完毕work2 " + str(num))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('test_gevent.py.py start'))
        start_time = time.time()
        # print(time.time())
        g_list = list()
        for _ in range(0, 10):
            g1 = gevent.spawn(self.work1, _)
            g_list.append(g1)
        g1 = gevent.spawn(self.work2, 11)
        g_list.append(g1)
        gevent.joinall(g_list)
        print('耗时')
        print(time.time() - start_time)
        self.stdout.write(self.style.SUCCESS('test_gevent.py.py ok'))
