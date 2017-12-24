__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time

###
import sys
sys.path.append("..")
import huadong
###

class P01_HachiLogin:
    def P01_HachiLogin(driver):
        #尝试关闭版本更新
        try:
            time.sleep(3)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()
        except Exception as e:
            print ("不需要取消更新")
            pass

        time.sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("我家")').click()
        #点击我家
        time.sleep(3)
        #点击未登录
        try:
            #case1:com.pujitech.pujiejia:id/tv_user_center_name
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_user_center_name").click()
        except:
            print ("case1:通过id查找失败")
            try:
                #case2:text:未登录
                driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("未登录")').click()
            except:
                print ("case2:通过android_uiautomator查找text失败")
                try:
                    #case3:XPTH___//android.widget.TextView[@text='未登录']
                    find_element_by_xpath('android.widget.TextView[@text="未登录"]').click()
                except:
                    print ("case3:通过xpath查找text失败")
                    try:
                        #case4:通过xpath2查找text失败
                        driver.find_element_by_xpath("//android.widget.TextView[contains(@text='未登录')]").click()
                    except:
                        print ("case4:通过xpath2查找text失败")
                        try:
                            #case5:driver.find_element_by_xpath("//*[contains(text(), '北京')]").click()
                            #driver.find_element_by_xpath("//*[contains(text(), '未登录')]").click()
                            #print ("case5:通过xpath模糊查找text失败")
                            #case6:通过坐标点击
                            driver.tap([214,210][346,262], 500)
                        except:
                            print ("case6:通过坐标点击失败")
                            pass



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

        #对登录后的页面进行截图
        import os
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\Screenshots\\'
        timestamp = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_folder + timestamp + "登录截图" + '.png'
        time.sleep(3)
        driver.get_screenshot_as_file(screen_save_path)

        #对登录后的页面进行断言判断是否登录成功
        username = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_user_center_phone")
        if username.text == '13263160105':
            print ("case is Pass")
        else:
            print ("case is Failed")

