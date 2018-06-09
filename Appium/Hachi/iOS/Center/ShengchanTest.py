__author__ = 'TANUKI'
#coding:utf-8
#生产版本的自动化测试

import sys, time
sys.path.append("..")
from appium import webdriver
#import os,time
from Public import testphone
#img_file = img_file.img_file()  #定义图片文件保存的位置
############导入测试用例###############
sys.path.append("../ReleasePage")
#from 文件名 import Class名
from Case01_Loginin import Loginin
from Case02_ShiDiPai import ShiDiPai
from Case03_MyHome import MyHome
from Case04_MyPurse import MyPurse
from Case05_MyCoupon import MyCoupon
from Case06_MyOrder import MyOrder
from Case07_MyAPP import MyAPP
from Case08_NeighborTalk import NeighborTalk
from FilePublic_Page import Public_Page

######################################

shouji = testphone.testphone()
#读取被测的手机型号
driver = webdriver.Remote('http://localhost:4723/wd/hub', shouji)




time.sleep(2)
print ("Fengyongming")
#driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
print ("Fengyongming002")
time.sleep(2)
allbutn = driver.find_elements_by_id("com.pujitech.pujiejia:id/fixed_bottom_navigation_title")
for target in allbutn:
    if target.text == "我家":
        target.click()