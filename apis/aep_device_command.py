#!/usr/bin/python
# encoding=utf-8


from apis.core import AepSdkRequestSend
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateCommand(appKey, appSecret, MasterKey, body):
    path = '/aep_device_command/command'
    head = {}
    param = {}
    version = '20190712225145'
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, appKey, MasterKey, appSecret, method='POST')
    print(response.status_code)
    if response is None:
        return None
    else:
        return response
