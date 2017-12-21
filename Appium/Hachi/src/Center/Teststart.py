__author__ = 'TANUKI'
#coding:utf-8
#开始的地方

import sys
sys.path.append("..")
from appium import webdriver
import os,time
from Public import testphone
#img_file = img_file.img_file()  #定义图片文件保存的位置
############导入测试用例###############
sys.path.append("../TestPage")
from P01_HachiLogin import P01_HachiLogin
from P02_Loginout import P02_Loginout
from P03_qiehuanloupan import P03_qiehuanloupan
######################################

shouji = testphone.testphone()
driver = webdriver.Remote('http://localhost:4723/wd/hub', shouji)

#P01_HachiLogin.P01_HachiLogin(driver)
#文件.类名(class).方法名

P03_qiehuanloupan.P03_qiehuanloupan(driver)

#driver.quit()