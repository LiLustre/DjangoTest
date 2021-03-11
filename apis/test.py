# import json
#
# from apis import aep_device_command
# body= json.dumps({
#   "content": {
#   		  "dataType":2,
#   	       "payload": "55AA00910000535EE3CD27698A3B8A4DC457E9BF574F2A174FB063130DF5BE7FF4729F503C4CA1D032E7CAF254E23074A10CB5C7400BA1D032E7CAF254E23074A10CB5C7400BA1D032E7CAF254E23074A10CB5C7400BA1D032E7CAF254E23074A10CB5C7400BA1D032E7CAF254E23074A10CB5C7400BA1D032E7CAF254E23074A10CB5C7400BA1D032E7CAF254E23074A10CB5C7400B9A55"
#   		    },
#   "deviceId": "ee05d82da0ad41ffbd717cd980e87284",
#   "operator": "camera_monitor_test",
#   "productId": "15031300",
#   "ttl": 7200,
#   "deviceGroupId": None,
#   "level": 1
# }, ensure_ascii=False)
#
# ###
# result = aep_device_command.CreateCommand('UMIzrWT83Rh', 'eOt6L0Mplx', '6ab1f4834c874d679716849e1762fc95', body)
# #result = aep_device_command.QueryCommand('UMIzrWT83Rh', 'eOt6L0Mplx', '6ab1f4834c874d679716849e1762fc95', '2',15031300,'ee05d82da0ad41ffbd717cd980e87284')
# print('result='+str(result.json()))
import base64

str(base64.b64encode(None), 'utf-8')