__author__ = 'TANUKI'
#coding:utf-8

from appium import webdriver
import os,time
import huadong
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['noReset'] = True  # 不需要每次都安装apk
desired_caps['deviceName'] = 'vivo-vivo_x9-be1bd33f'  # vivo Y51A
desired_caps['resetKeyboard'] = 'True'
desired_caps['appPackage'] = 'com.lovebizhi.wallpaper'
desired_caps['appActivity'] = 'com.adesk.picasso.view.MainActivity'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(15)
driver.close_app()

while 1:
    time.sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("一键换壁纸")').click()
    #driver.tap([313,1312][511,1510], 500)
