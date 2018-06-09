__author__ = 'TANUKI'
#coding:utf-8
import sys
sys.path.append("..")
import os
import yaml
from Public import information


def testphone():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
    #print ("当前项目的根路径为：",path)
    f = open( path + '/Public/test_phone.yaml', 'rb')
    files = yaml.load(f)
    f.close()
    file = files['Phone']
    if file == 'iPhone6':
        shouji = information.iPhone6()
    elif file == 'VIVO_X9':
        shouji = information.VIVO_X9()
    elif file == 'huawei_NOT8':
        shouji = information.huawei_NOT8()
    elif file == 'huawei_P9':
        shouji = information.huawei_P9()
    elif file == 'hw_honor_V9':
        shouji = information.hw_honor_P9()
    else:
        print('您在test_phone.yaml输入的测试机没有相关信息')
        shouji = '空'
    #print('获取到用来测试的手机信息为：%s' %shouji)
    return shouji
