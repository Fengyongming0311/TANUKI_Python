#coding:utf-8
#测试用webservice:http://ws.webxml.com.cn/WebServices/TranslatorWebService.asmx?wsdl


from suds.client import Client

url = 'http://ws.webxml.com.cn/WebServices/TranslatorWebService.asmx?wsdl'
#中英文互翻译接口,麻痹，问号得转义哈哈哈
#这里填写接口地址
client = Client(url)


#下查看service提供的方法
#print (client)

'''
#方法1
result = client.service.getEnCnTwoWayTranslator("apple")
print (result)
'''

'''
#方法2
result = client.service.getEnCnTwoWayTranslator(Word = "apple")
print (result)
'''

'''
#方法3

'''

'''
Types (1):
        ArrayOfString
'''
person = client.factory.create('ArrayOfString')
#print (person)
#这里是用的接口中的哪个方法


#传递对象参数(复杂参数)
#print (person.__dir__())


#下面二选一
person.string.append('apple')
#这里传参数
#person.string = "apple"
#print (person.string)


'''
下面是打印结果的...
'''
try:  
   person_added = client.service.getEnCnTwoWayTranslator(person)
   print (person_added)
except Exception as e:  
  print (e)



'''
client = Client(url,faults=False)
result=client.service.ClassIn("apple")
print (result)
'''



