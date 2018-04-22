__author__ = 'TANUKI'
#coding:utf-8
import sys
sys.path.append("..")
import os, yaml
from Public import information


def testphone():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
    #print ("当前项目的根路径为：",path)
    f = open( path + '\\Public\\test_phone.yaml', 'rb')
    files = yaml.load(f)
    f.close()
    file = files['Phone']
    if file == 'VIVO':
        shouji = information.VIVO()
    #手头上还没有其他手机...
    elif file == 'NOTE2':
        shouji = information.NOTE2()
    else:
        print('您在test_phone.yaml输入的测试机没有相关信息')
        shouji = '空'
    #print('获取到用来测试的手机信息为：%s' %shouji)
    return shouji
