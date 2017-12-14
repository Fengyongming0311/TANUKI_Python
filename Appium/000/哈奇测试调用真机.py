#coding=utf-8
from appium import webdriver
import time
desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'vivo-vivo_x9-be1bd33f'

desired_caps['appPackage'] = 'com.pujitech.pujiejia'
#appPackage：待测试的 app 的 java package。比如 com.example.android.myApp, com.android.settings。
desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
#appActivity：待测试的 app 的 Activity 名字。比如 MainActivity, .Settings。注意，原生 app 的话要在 activity 前加个"."。
'''
launchable-activity: name='com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
'''
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




time.sleep(5)

driver.find_element_by_name("我家").click()
#com.pujitech.pujiejia:id/fixed_bottom_navigation_icon我家
time.sleep(1)
driver.find_element_by_name("未登录").click()

time.sleep(1)
driver.find_element_by_id("com.pujitech.pujiejia:id/et_login_username").send_keys("13263160105")
#com.pujitech.pujiejia:id/et_login_username

time.sleep(1)
driver.find_element_by_id("com.pujitech.pujiejia:id/et_login_password").send_keys("00000000")

time.sleep(1)
driver.find_element_by_id("com.pujitech.pujiejia:id/btn_login").click()
#com.pujitech.pujiejia:id/btn_login

###登出
time.sleep(5)
driver.find_element_by_id("com.pujitech.pujiejia:id/iv_setting").click()
#settings
#com.pujitech.pujiejia:id/iv_setting

time.sleep(1)
driver.find_element_by_id("com.pujitech.pujiejia:id/rl_login_out").click()
#com.pujitech.pujiejia:id/rl_login_out
#退出按钮

time.sleep(1)
driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
#com.pujitech.pujiejia:id/tv_confirm
#二次确认