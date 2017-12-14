#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode


 
def main():
    Test("GET")
 
 
 
#手机归属地查询
#m="GET" 看接口类型如果需要POST 改为m="POST"
def Test(m="POST"):
    url = "https://mapi.baocai.com/auth/register/phone/code"
    #这个是请求接口地址，适用于url的接口
    params = {
        "phone" : "13511111117", #手机号码
        }
    #params 是请求的参数
    params = urlencode(params)
    #上面把参数进行编码 
    #如果是POST这里也得改为POST
    if m =="POST":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    #这里配置连接
    res = json.loads(content)

    print (res)
    '''
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"
    '''
 
 
 
if __name__ == '__main__':
    main()
