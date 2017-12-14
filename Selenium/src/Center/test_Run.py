__author__ = 'TANUKI'
#coding:utf-8
import start
from selenium import webdriver
import sys,time
sys.path.append('../TestPage/')

from Z01_LoginPage import Z01_LoginPage
from Z02_Addshangjia import Z02_Addshangjia
from Z03_Addyouhuiquan import Z03_Addyouhuiquan
from Z09_LoginOut import Z09_LoginOut


'''
可以做的页面
商家管理---商家信息---添加商家

广告管理---发布管理---添加新广告

运营管理---优惠券管理---添加新优惠券
        ---团购管理---添加新团购

（社圈管理---发言管理---发言）

其他页面可做查询

'''


driver = webdriver.Firefox()
driver.get(start.login_url)

#Run 登录
Z01_LoginPage.LoginPage(driver)

Z02_Addshangjia.Addshangjia(driver)

#Z03_Addyouhuiquan.Addyouhuiquan(driver)

#登出
#Z09_LoginOut.LoginOut(driver)