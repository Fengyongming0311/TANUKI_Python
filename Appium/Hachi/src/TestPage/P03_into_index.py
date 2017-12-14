__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time
'''
case：进入首页点击中山璟湖城进入切换城市
'''
class P03_into_index:
    def P03_into_index(driver):
        #尝试关闭版本更新
        try:
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()
        except Exception as e:
            print ("不需要取消更新")
            pass

        try:
            time.sleep(1)
            #点击首页
            driver.find_element_by_android_uiautomator("首页").click()

            time.sleep(1)
            #driver.find_element_by_android_uiautomator('newUiSelector().description("中山璟湖城")').click()
            driver.find_element_by_android_uiautomator("中山璟湖城").click()

            time.sleep(8)


            #可能需要switch
            don = driver.contexts

            print (don)


            driver.switch_to.context('NATIVE_APP')

            buttons = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_city")
            #通过id
            #com.pujitech.pujiejia:id/tv_city
            print (buttons)

            buttons.pop(1).click()
            #buttons = driver.find_elements_by_class_name("android.widget.TextView")
            time.sleep(1)
            #print (buttons)
            #buttons.pop(0).click()

            driver.find_element_by_android_uiautomator("无锡丁香雅苑").click()

            time.sleep(5)

            #进入城市列表选择---无锡
        except Exception as e:
            print (e)
            pass
