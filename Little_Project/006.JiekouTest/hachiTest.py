#coding:utf-8

import requests

url = 'http://218.28.28.186:9088/ehomeapp/app/common/getCities'

r = requests.get(url)

print (r.status_code)

print (r.text)