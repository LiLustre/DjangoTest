from django.test import TestCase

# Create your tests here.
import random

from django.test import TestCase

# Create your tests here.
# gevent的好处：能够自动识别程序中的耗时操作，在耗时的时候自动切换到其他任务
from gevent import monkey
monkey.patch_all(thread=False)

import time
import gevent
# from greenlet import greenlet
# greenlet可以实现一个自行调度的微线程
def work1(num):
        print("正在执行work1（）"+str(num))
        print(time.time())
        # time.sleep(0.5)#模拟阻塞        默认情况下，time.sleep不能够被gevent识别为耗时操作，因此可以用gevent.sleep
        # gevent.sleep(0.5)
#      但是就是想用time.sleep，需要进行下面操作
#         进行打补丁
#         1.导入monkey模块
#         2.破解  monkey.patch_all()
        time.sleep(random.randint(0,5))
        print("执行完毕 "+str(num))

if __name__ == '__main__':
    # 创建gevent的对象    gevent.spawn（函数名,参数1，参数2.。。。）
    while True:
        start_time=time.time()
        #print(time.time())
        g_list = list()
        for _ in range(0, 10):
            g1= gevent.spawn(work1,_)
            g_list.append(g1)
        gevent.joinall(g_list)
        print('耗时')
        print(time.time()-start_time)


    # while True:
    #     print('开始-----------------------')
    #     for _ in range(0,10):
    #         g1= gevent.spawn(work1,_)
    #
    #         g1.join()
