__author__ = 'TANUKI'
#coding:utf-8
#from appium import webdriver
import time

###
import sys
sys.path.append("..")
from Case03_MyHome import MyHome
from FilePublic_Page import Public_Page
import huadong
###
class Loginin:
    def OnceInto(driver):
        try:
            try:
                driver.wait_activity(".modules.splash.views.activities.GuideActivity", 30)
                time.sleep(1)
            except:
                time.sleep(5)
                pass

            i = 0
            while(i<4):
                time.sleep(2)
                huadong.zuohua(driver, 1000)
                print ("第%s次滑动结束..."%(i+1))
                i = i + 1
        except:
            print ("进入异常FYM")

    #第一次进入的账号登录
    def OnceIntoLogin(driver):
        try:
            try:
                driver.wait_activity(".modules.splash.views.activities.GuideActivity", 30)
                time.sleep(1)
            except:
                time.sleep(5)
                pass
            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_to_login").click()
            #点击登录按钮
            result = Public_Page.DengLu(driver, 13263160105, "00000000")

            if result == True:
                print("执行用例..............................登录哈奇账户成功")
            else:
                print("执行用例..............................登录哈奇账户失败")
        except:
            print ("执行用例..............................登录哈奇账户失败")
            pass

    def OnceChoiceBuilding(driver, Building):
        """
        第一次选择楼盘
        :param Building: 传入楼盘名称
        :return: None
        """
        try:
            Public_Page.ChoiceBuilding(driver, Building)
            print ("执行用例..............................选择楼盘%s成功"%Building)

        except:
            print ("执行用例..............................选择楼盘%s失败"%Building)
            pass

    def Loginin_nomal(driver, username, password):
        """
        测试平时登录账户(在已有楼盘下账户未登录状态)
        :param username: 手机号
        :param password: 密码必须传入字符串"00000000"
        :return:None
        """
        try:
            MyHome.IntoDengLuPage(driver)
            jieguo = Public_Page.DengLu(driver, username, password)
            if jieguo == True:
                print("执行用例..............................登录哈奇账户%s成功"%username)
            else:
                print("执行用例..............................登录哈奇账户%s失败"%username)
        except:
            pass


    def Loginin_Switch_ID(driver, username, password):
        Public_Page.Switch_Navigation(driver, tab = "我家")
        #点击我家
        time.sleep(3)
        try:
            userphone = driver.find_element_by_id('com.pujitech.pujiejia:id/tv_user_center_phone')
            if not userphone.text == str(username):
                Public_Page.Dengchu(driver)
                Loginin.Loginin_nomal(driver, username, password)
        except Exception as e:
            print (e)
            pass





