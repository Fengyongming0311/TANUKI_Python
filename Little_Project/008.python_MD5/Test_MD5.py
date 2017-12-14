__author__ = 'TANUKI'
#coding:utf-8
import hashlib

m = hashlib.md5()

pwd = "I love You"

m.update(pwd.encode('utf-8'))

word = m.hexdigest()
#print (word)
#打印出加密后的md5信息

def md5(_str):
    import hashlib
    m = hashlib.md5()
    m
