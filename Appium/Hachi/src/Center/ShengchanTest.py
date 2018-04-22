__author__ = 'TANUKI'
#coding:utf-8
#生产版本的自动化测试

import sys
sys.path.append("..")
from appium import webdriver
import os,time
from Public import testphone
#img_file = img_file.img_file()  #定义图片文件保存的位置
############导入测试用例###############
sys.path.append("../ReleasePage")
#from 文件名 import Class名
from Case01_Loginin import Loginin
from Case02_IndexTap import IndexTap
from Case03_MyHome import MyHome
######################################

shouji = testphone.testphone()
driver = webdriver.Remote('http://localhost:4723/wd/hub', shouji)

#Loginin.Loginin_one(driver)
#测试第一次登录

#IndexTap.IndexTap_one(driver)
#测试首页各个功能

MyHome.MyHome_one(driver)
#MyHome.MyHome_two(driver)
MyHome.MyHome_three(driver)
#测试我家页面中各个功能
