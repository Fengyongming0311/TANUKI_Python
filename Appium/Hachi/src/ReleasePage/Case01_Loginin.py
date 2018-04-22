__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time

###
import sys
sys.path.append("..")
import huadong
###

class Loginin:
    def Loginin_one(driver):
        try:
            time.sleep(8)
            i = 0
            while(i<4):
                time.sleep(2)
                huadong.zuohua(driver, 1000)
                print ("第%s次滑动结束..."%(i+1))
                i = i + 1
        except:
            print ("进入异常FYM")
        try:
            time.sleep(5)
            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_to_login").click()
            #点击登录按钮
            #com.pujitech.pujiejia:id/btn_to_login
            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/et_login_username").send_keys("13263160105")
            #输入用户名
            #com.pujitech.pujiejia:id/et_login_username

            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/et_login_password").send_keys("00000000")
            #输入密码
            #com.pujitech.pujiejia:id/et_login_password

            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_login").click()
            #com.pujitech.pujiejia:id/btn_login
            #点击立即登录
        except:
            print ("不执行这步")
            pass

        try:
            time.sleep(3)
            #case1
            #driver.find_element_by_xpath("//*[@text='中山璟湖城']").click()

            #case2: 只有原生
            #ct = driver.contexts
            #print (ct)

            #case3:得到当前 Activity
            #cct = driver.current_activity
            #print (cct)

            #case4
            #buttons = driver.find_elements_by_class_name("android.support.v7.widget.RecyclerView")
            #buttons.find_element_by_android_uiautomator('new UiSelector().text("中山璟湖城")').click()

            #case5
            #buttons = driver.find_elements_by_class_name("android.support.v7.widget.RecyclerView")
            #buttons.find_element_by_xpath("//android.widget.TextView[contains(@index,'5')]").click()

            #case6
            #driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView[0]").click()

            #case7 tap
            driver.tap([(0,1236), (964,1363)], 500) #哈奇内部测试

            print ("pass")
        except:
            print ("执行用例失败")
            pass