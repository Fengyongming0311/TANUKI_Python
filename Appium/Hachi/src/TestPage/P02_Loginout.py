__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time

class P02_Loginout:
    def P02_Loginout(driver):
        try:
            time.sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().text("我家")').click()
            #点击我家
			#driver.tap([(936,1794),(1008,1866)], 500)
            time.sleep(1)
            driver.find_element_by_id('com.pujitech.pujiejia:id/iv_setting').click()
            #点击setting___com.pujitech.pujiejia:id/iv_setting
            time.sleep(1)
            driver.find_element_by_id('com.pujitech.pujiejia:id/rl_login_out').click()
            #点击退出按钮___com.pujitech.pujiejia:id/rl_login_out
            time.sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("确认")').click()
            #二次确认___确认
        except:
            pass
