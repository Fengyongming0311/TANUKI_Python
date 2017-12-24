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

            '''
            ###下看在哪个activity
            current = driver.current_activity
            print(current)
            ###下获取当前页面代码
            page = driver.page_source
            print (page)

            '''
            #点击其他楼盘名称
            time.sleep(3)
            #case1__android_uiautomator:遵义·遵义蔷薇国际
            #driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("遵义·遵义蔷薇国际")').click()

            #case2__textContains("View")
            #driver.find_element_by_android_uiautomator('new UiSelector().textContains("中山璟湖城")').click()

            #case3__xpath
            #driver.find_element_by_xpath("//android.widget.TextView[contains(@text='中山璟湖城')]").click()

            #case4__text(\"中山璟湖城\")
            #driver.find_element_by_android_uiautomator('new UiSelector().text(\"中山璟湖城\")').click()

            #case5__index
            #driver.find_element_by_android_uiautomator('new UiSelector().index(\"4\")').click()

            #case6__.clickable(true).index("4")
            #driver.find_element_by_android_uiautomator('new UiSelector().clickable(true).index("4")').click()

            #case7__elements  _accessibility_id
            #dondake = driver.find_elements_by_accessibility_id("com.pujitech.pujiejia:id/tv_city")

            #case8__elements  _classname
            #dondake = driver.find_elements_by_class_name("android.widget.RelativeLayout")
            #print (dondake)
            #dondake.pop(0).click()

            #case9__elements  _classname__
            #dondake = driver.find_elements_by_class_name("android.widget.TextView")
            #print (dondake)
            #dondake.pop(0).click()

            #case10__直接tap  这个可以点,输入要点击小区的坐标
            #driver.tap([(0,729), (1080,856)], 500) #中山
            driver.tap([(0,221), (1080,348)], 500) #测试


        except Exception as e:
            print (e)
            pass
