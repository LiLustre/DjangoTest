#!/usr/bin/python
# encoding=utf-8
import base64
import datetime
# import urllib2
import hmac
import time
from hashlib import sha1
import requests
from urllib.parse import urlencode
import urllib.request as urllib2


def sendSDKRequest(path, head, param, body, version, application, MasterKey, key, method = None, isNeedSort = True, isNeedGetTimeOffset = False):
    #header 构造
    paramList=[]
    for key_value in param:
        paramList.append([key_value, param[key_value]])
    if (MasterKey is not None) and (MasterKey.strip()) :
        paramList.append(['MasterKey',MasterKey])
    if isNeedSort:
        paramList = sorted(paramList)
    headers = {}
    if (MasterKey is not None) and (MasterKey.strip()) :
        headers['MasterKey'] = MasterKey
    headers['application'] = application
    headers['Date'] = str(datetime.datetime.now())
    headers['version'] = version
    global offset
    if isNeedGetTimeOffset:
        offset = getTimeOffset(timeUrl)
    timestamp = str(int(time.time()*1000) + offset)
    headers['timestamp'] = timestamp
    sign = signature(key, application, timestamp, paramList, body)
    headers['signature'] = sign
    headers.update(head)
    #url构造
    temp = dict(param.items())
    if (MasterKey is not None) and (MasterKey.strip()):
        temp['MasterKey'] = MasterKey
    url_params = urlencode(temp)
    url = baseUrl + path
    if (url_params is not None) and (url_params.strip()):
        url = url + '?' + url_params
    resp = requests.request(method,
        url=url,
        headers=headers,
        data=body.encode('utf-8'),
        timeout=60,
    )
    return resp


# key、application、timestamp、body为字符串
# param为list，结构如下
# param=[['deviceId', '1'], ['deviceName', 'test']]
def signature(key, application, timestamp, param, body):
    code = "application:" + application + "\n" + "timestamp:" + timestamp + "\n"
    for v in param:
        code += str(v[0]) + ":" + str(v[1]) + "\n"
    if (body is not None) and (body.strip()):
        code += body + '\n'
    print("param=" + str(param))
    print("body=" + str(body))
    print("code=" + str(code))

    return base64.b64encode(hash_hmac(key, code, sha1))


def hash_hmac(key, code, sha1):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1)
    print("hmac_code=" + str(hmac_code.hexdigest()))
    return hmac_code.digest()


def getTimeOffset(url):
    request = urllib2.Request(url)
    start = int(time.time() * 1000)
    response = urllib2.urlopen(request)
    end = int(time.time() * 1000)

    if response is not None:
        return int(int(response.headers['x-ag-timestamp']) - (end + start) / 2);
    else:
        return 0


baseUrl = 'https://ag-api.ctwing.cn'
timeUrl = 'https://ag-api.ctwing.cn/echo'
offset = getTimeOffset(timeUrl)

# path为baseUrl后面的路径地址字符串，param用字典,body为字符串(可以为空字符串或者None,为空时，默认为get请求),version为字符串(需要去api页面查询),application、MasterKey、key为字符串
# path = '/aep_device/dm/device/v1/getDeviceInfo'
# head = {'tenantId':'10003'}
# param = {'MasterKey':'25ce00cc28c1498c833276110ee483f0'}
# body = '{"pageNow":0,"pageSize":100,"productId":9392,"searchValue":"","tenantId":"10017447"}'
# version = '20180717143941'
# application = '91Ebv1S0HBb'
# MasterKey = '25ce00cc28c1498c833276110ee483f0'
# key = "FJDq8agNp5"
# 广研的算法里貌似对param有个默认字典序排序，如果需要排序，isNeedSort传True