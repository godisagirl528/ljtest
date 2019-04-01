"""
    requests入门
    1. get/post/传参/xrld读取excel实现数据驱动
"""

import requests

url = "http://lux.itblacklist.top/"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "b668f567-997c-41b0-a775-d74bdab6d559"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)