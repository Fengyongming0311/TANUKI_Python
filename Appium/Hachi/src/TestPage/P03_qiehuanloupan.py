__author__ = 'TANUKI'
#coding:utf-8
import time
import huadong
'''
case：进入首页点击中山璟湖城进入切换城市
'''
class P03_qiehuanloupan:
    def P03_qiehuanloupan(driver):
        #尝试关闭版本更新
        try:
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()
        except Exception as e:
            print ("不需要取消更新")
            pass

        try:
            time.sleep(5)
            huadong.shanghua(driver, 1000)
            #下滑页面
            time.sleep(1)
            #点击实地派
            driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("实地派")').click()

            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/rl_building_name_container").click()
            #com.pujitech.pujiejia:id/rl_building_name_container
            #com.pujitech.pujiejia:id/tv_building_name
            #com.pujitech.pujiejia:id/bg_building
            #进入选择楼盘

            ###ct = driver.contexts
            ###print (ct)
            #查看上下文
            ###driver.switch_to.context('WEBVIEW_com.pujitech.pujiejia')
            #driver.switch_to.context('WEBVIEW_com.pujitech.pujiejia:pushcore')
            #点击其他楼盘名称

            current = driver.current_activity
            print(current)

            page = driver.page_source
            print(page)
            ###看在哪个activity
            #case1__android_uiautomator:遵义·遵义蔷薇国际
            #driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("遵义·遵义蔷薇国际")').click()
            time.sleep(3)
            #case2__textContains("View")
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("中山璟湖城")').click()

            #case3__xpath
            #driver.find_element_by_xpath("//android.widget.TextView[contains(@text='中山璟湖城')]").click()

        except Exception as e:
            print (e)
            pass
