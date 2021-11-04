from uuid import uuid4

from requests_toolbelt import MultipartEncoder

m = MultipartEncoder(fields={})
print(uuid4().hex)