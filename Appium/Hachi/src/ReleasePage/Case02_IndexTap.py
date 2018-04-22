__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time

###
import sys
sys.path.append("..")
import huadong
###

class IndexTap:
    def IndexTap_one(driver):
        '''
        先点击实地派按钮进入首页页面
        '''
        tab = "实地派"
        try:
            time.sleep(3)
            allbutn = driver.find_elements_by_id("com.pujitech.pujiejia:id/fixed_bottom_navigation_title")
            for target in allbutn:
                if target.text == tab:
                    target.click()
                    break
                #点完了就跳出循环，否则会再次找寻case内容导致报错
        except:
            print ("未切换到我家页面，程序退出....")
            quit()


        time.sleep(5)
        case = "餐饮美食"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(5)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass



        #测试消费分期是否可以进入
        time.sleep(3)
        case = "消费分期"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == '握手分期':
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass



        #测试智能家居是否可以进入
        time.sleep(3)
        case = "智能家居"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_base_title")
            if checkpoint.text == case or checkpoint.text == '我的网关':
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass


        #测试物业缴费是否可以进入
        time.sleep(3)
        case = "物业缴费"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass



        #测试投诉建议是否可以进入
        time.sleep(3)
        case = "投诉建议"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(5)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_content")
            if checkpoint.text == "您没有在该小区认证房间":
                print ("点击投诉建议后提示：",checkpoint.text)
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            pass
        finally:
            try:
                driver.tap([(900,1200)], 500)
                #点击一下白屏幕，不然焦点丢失，无法到当前页面
            except:
                pass


        #测试限时促销是否可以进入
        time.sleep(5)
        case = "限时促销"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(5)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass


        #############
        #更多功能先不点呢
        #############


        #测试实地派会员广告图片是否可以进入
        time.sleep(3)
        case = "实地派会员专享权益"
        try:
            driver.find_element_by_id('com.pujitech.pujiejia:id/iv_brand_image').click()
            time.sleep(5)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass




        #测试尊享服务中智能家居是否可以进入
        time.sleep(3)
        case = "智能家居"
        try:
            dower = driver.find_elements_by_android_uiautomator('new UiSelector().text("%s")'%case)
            dower.pop(1).click()
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_base_title")
            if checkpoint.text == case or checkpoint.text == '我的网关':
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass


        #测试消费分期是否可以进入
        time.sleep(3)
        case = "消费分期"
        try:
            dower = driver.find_elements_by_android_uiautomator('new UiSelector().text("%s")'%case)
            dower.pop(1).click()
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == '握手分期':
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass


        #测试专享活动是否可以进入
        time.sleep(5)
        case = "专享活动"
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
            time.sleep(5)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)
            pass

        """
        页面出现两个智能家居如何定位的debug
        time.sleep(5)
        dondake = driver.find_elements_by_android_uiautomator('new UiSelector().text("智能家居")')
        print (dondake)
        print (dondake[0].text)
        print (dondake[1].text)
        """



        #############
        #开始下滑页面到下一页
        #############
        time.sleep(5)
        huadong.shanghua(driver, 300)
        #点击图片广告广州常春藤
        time.sleep(3)
        case = "图片广告广州常春藤楼盘"
        try:
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_community_image").click()
            #滑动查看常春藤
            time.sleep(2)
            huadong.shanghua(driver, 300)

            time.sleep(2)
            huadong.shanghua(driver, 300)

            driver.back()
            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)


        #点击推荐楼盘无锡玫瑰庄园
        time.sleep(3)
        case = "无锡玫瑰庄园"
        try:
            lpan = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_community_name")

            for target in lpan:
                #print (target.text)
                if target.text == case:
                    target.click()
                    break
                    #点完了就跳出循环，否则会再次找寻case内容导致报错

            #向上滑动查看页面
            time.sleep(2)
            huadong.shanghua(driver, 500)
            time.sleep(2)
            huadong.xiahua(driver, 500)

            time.sleep(5)
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)
            driver.tap([(900,1200)], 500)



        #点击更多楼盘，进入精品楼盘页面查看
        time.sleep(3)
        huadong.shanghua(driver, 800)
        case = "精品楼盘"
        try:
            #driver.find_elements_by_id("com.pujitech.pujiejia:id/ll_more_community").click()
            driver.find_element_by_android_uiautomator('new UiSelector().text("更多楼盘")').click()

            #向上滑动查看页面
            time.sleep(4)
            huadong.shanghua(driver, 800)
            time.sleep(2)
            huadong.xiahua(driver, 800)

            time.sleep(2)
            #chickp = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_title")
            chickp = driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case)

            if chickp.text == case:
                time.sleep(3)
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)
            time.sleep(2)






