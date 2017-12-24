__author__ = 'TANUKI'
#coding:utf-8
import time
import huadong
'''
case：进入生活购页面
'''
class P05_shenghuogou:
    def P05_shenghuogou(driver):
        try:
            time.sleep(5)

            driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("生活购")').click()



        except Exception as e:
            print (e)
            pass

