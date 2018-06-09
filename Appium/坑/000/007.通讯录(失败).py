#coding=utf-8
from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.example.android.contactmanager'
desired_caps['appActivity'] = '.ContactManager'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)