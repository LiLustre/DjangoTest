from uuid import uuid4

from requests_toolbelt import MultipartEncoder
#1.2.0
m = MultipartEncoder(fields={})
print(uuid4().hex)