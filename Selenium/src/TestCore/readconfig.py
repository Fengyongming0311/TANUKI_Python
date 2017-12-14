__author__ = 'TANUKI'
#coding:utf-8
import sys
#sys.path.append('../../config/')
import configparser
'''
在方法中定义全局变量
用global 就可以了
'''

#读取配置文件config.ini，里面存了一些配置信息
def get_config():
    config = configparser.ConfigParser()
    config_file = open('../../config/config.ini')
    config.readfp(config_file)
    config_file.close()

    return config