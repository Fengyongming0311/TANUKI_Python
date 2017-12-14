__author__ = 'TANUKI'
#coding:utf-8

from appium import webdriver
import os,time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['noReset'] = True  # 不需要每次都安装apk
desired_caps['deviceName'] = 'vivo-vivo_x9-be1bd33f'  # vivo Y51A
desired_caps['resetKeyboard'] = 'True'
desired_caps['appPackage'] = 'com.pujitech.pujiejia'
desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)
print ("kaishi")
#android.widget.TextView
#driver.find_element_by_name("下次更新").click()
driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()
print ("jieshu")