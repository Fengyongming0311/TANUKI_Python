#coding=utf-8
from appium import webdriver

desired_caps = {
'platformName': 'Android',
'platformVersion': '4.4.2',
'deviceName': 'Android Emulator',
'browserName': 'Browser',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print ("start baidu page!")

driver.get('http://www.baidu.com')


driver.get('http://www.jd.com')