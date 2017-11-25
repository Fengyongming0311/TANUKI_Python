import os

from appium import webdriver

#from selenium import webdriver

import time

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}

desired_caps['deviceName'] = 'be1bd33f'#设备明，在terminal窗口使用 adb devices命令得到

desired_caps['platformName'] = 'Android'#系统
desired_caps['browserName'] = '4.4.2'
desired_caps['platformVersion'] = '7.1.1' #系统版本号
#D:\hachi1.0.2.apk
#desired_caps['app'] = 'D:\\hachi1.0.2.apk'
#desired_caps['AppWaitActivity'] = '.ui.startup.role.RoleActivity'




#desired_caps['appPackage'] = 'com.pujitech.pujiejia'
#desired_caps['appActivity'] = 'com.meituan.android.tower.reuse.holiday.HolidayNativeHomepageActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.quit()