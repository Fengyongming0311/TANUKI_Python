#coding:utf-8

import requests

url = 'http://218.28.28.186:9088/ehomeapp/app/common/saveUserBuilding'

data = {'userID': '7233be4eea3f45e985ed0f25ab7cde82','buildingID':'2'}

re = requests.post(url, data=data)

print (re.text)



'''
#出处http://blog.csdn.net/shanzhizi/article/details/50903748
#上传文件
import requests

url = 'http://127.0.0.1:5000/upload'
files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
#files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名

r = requests.post(url, files=files)
print(r.text)
'''
