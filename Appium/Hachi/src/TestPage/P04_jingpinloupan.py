__author__ = 'TANUKI'
#coding:utf-8
import time
import huadong
'''
case：首页进入精品楼盘
'''
class P04_jingpinloupan:
    def P04_jingpinloupan(driver):
        try:
            time.sleep(5)
            #case1:com.pujitech.pujiejia:id/tv_app_name
            #dondake = driver.find_elements_by_accessibility_id("com.pujitech.pujiejia:id/tv_app_name")
            #print (dondake)

            #case2:精品楼盘
            driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text(\"精品楼盘\")').click()

            ###之后是H5页面


        except Exception as e:
            print (e)
            pass

