__author__ = 'TANUKI'
#coding:utf-8

#import os,time
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys     #引用Key包
#from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
#from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
#调用不同目录下的py文件
import sys
sys.path.append('../TestCore/')
import readconfig
#import Selenium.src.TestCore.readconfig PASS
#上 读取配置文件


##################################
#读取配置文件内容
web_config = readconfig.get_config()
login_url = web_config.get('config','zhsqurl')
logout_url = web_config.get('config','zhsqloginout')
username = web_config.get('config','username')
passwd = web_config.get('config','passwd')
tupianpath = web_config.get('config','tupianpath')
#这个设置上传图片路径的配置
##################################


