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
desired_caps['appPackage'] = 'com.hachi.smarthome'
desired_caps['appActivity'] = 'com.hachi.smarthome.modules.splash.view.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def denglu(i):
    time.sleep(5)
    driver.find_element_by_id("com.hachi.smarthome:id/et_user_phone").send_keys(i)


    time.sleep(3)
    driver.find_element_by_id("com.hachi.smarthome:id/et_user_password").send_keys("11111111")

    time.sleep(2)
    driver.tap([(25,500),(1000,756)], 100)
    time.sleep(5)

    driver.find_element_by_id("com.hachi.smarthome:id/btn_login").click()
    time.sleep(5)

def qiyong():
    time.sleep(3)
    driver.find_element_by_id("com.hachi.smarthome:id/tv_default_add_equipment").click()
    #jinshebei

    time.sleep(3)
    driver.tap([(347,304),(992,520)], 100)

    time.sleep(3)
    driver.tap([(935,442),(1045,506)], 100)
    #qiyong
    #[935,442][1045,506]
    try:
        time.sleep(3)
        driver.find_element_by_id("com.hachi.smarthome:id/tv_confirm").click()
        #queding
        time.sleep(5)

    except Exception as e:
        time.sleep(3)
        driver.tap([(44,102),(86,168)], 100)
        #点两下返回
        #[44,102][86,168]


        time.sleep(3)
        driver.tap([(44,102),(86,168)], 100)
        pass


def tuichu():
    time.sleep(3)
    driver.tap([(864,1776),(936,1848)], 100)
    #wode



    time.sleep(2)
    driver.tap([(175,1310),(981,1418)], 100)
    #shezhi

    time.sleep(2)
    driver.find_element_by_id("com.hachi.smarthome:id/logout").click()


    time.sleep(2)
    driver.find_element_by_id("com.hachi.smarthome:id/tv_confirm").click()


number = open("number.txt", "r")
phone = number.readlines()
number.close()

for i in phone:
    denglu(i)
    #qiyong()
    tuichu()









