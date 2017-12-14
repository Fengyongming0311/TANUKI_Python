#coding=utf-8
#自己尝试定位元素
from appium import webdriver
'''
desired_caps = {'platformName':'Android',
	'platformVersion':'4.4.2',
	'deviceName':'Android Emulator',
	'browserName':'Browser',}
'''
desired_caps = {}

desired_caps['platformName'] = 'Android'
#platformName  使用哪种平台 安卓还是iOS
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
#deviceName   启动哪种设备是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator, Galaxy S4, etc...

desired_caps['browserName'] = 'Browser'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

print ("start baidu page!")
driver.get('www.baidu.com')