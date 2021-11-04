import hashlib
import json
import random
import time
import requests

def md5_hex_digest(value, encoding="raw_unicode_escape"):
    h = hashlib.md5(value.encode(encoding))
    return h.hexdigest()

resp = requests.delete(

    url='https://camera-monitor-server.parkone.cn//api/deployment/projects/15f4303cb9fb11ebb8896a8ef6ec0836/cameras/862167057525374',
    headers={
        'X-CLIENT-ID': '093914c219c211eba6a8309c23a22f10',
        'X-CLIENT-MD5': md5_hex_digest('093914c219c211eba6a8309c23a22f10'+'093914c319c211eba6a8309c23a22f10')
    },
    timeout=10,
)
# resp = requests.get(
#             url='https://camera-monitor-server.parkone.cn/cameras/862167058977350-1/lastest_image',
#             headers={
#                             'X-CLIENT-ID': '03914c219c211eba6a8309c23a22f10',
#                             'X-CLIENT-MD5': md5_hex_digest(
#                                 '%s%s' % ('093914c219c211eba6a8309c23a22f10', '093914c319c211eba6a8309c23a22f10'),
#                             )
#                         },
#
#             params={
#                 'last_img_url_time': None
#             },
#             timeout=10,
#         )
print(resp.status_code)