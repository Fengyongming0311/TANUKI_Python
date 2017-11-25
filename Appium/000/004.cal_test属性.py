#coding=utf-8
from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'

desired_caps['appPackage'] = 'com.android.calculator2'
#appPackage：待测试的 app 的 java package。比如 com.example.android.myApp, com.android.settings。
desired_caps['appActivity'] = '.Calculator'
#appActivity：待测试的 app 的 Activity 名字。比如 MainActivity, .Settings。注意，原生 app 的话要在 activity 前加个"."。

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()