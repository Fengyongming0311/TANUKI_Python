#coding:utf-8
from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


driver.find_element_by_name("Language & input").click()