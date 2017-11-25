#coding=utf-8
from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'be1bd33f'

desired_caps['appPackage'] = 'com.bbk.launcher2'
#appPackage：待测试的 app 的 java package。比如 com.example.android.myApp, com.android.settings。
desired_caps['appActivity'] = '.Calculator'
#appActivity：待测试的 app 的 Activity 名字。比如 MainActivity, .Settings。注意，原生 app 的话要在 activity 前加个"."。

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#driver.find_element_by_id("com.bbk.launcher2:id/item_icon").click()