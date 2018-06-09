__author__ = 'TANUKI'
#coding:utf-8
import time
###
import sys
sys.path.append("..")
from FilePublic_Page import Public_Page
import huadong
import random
###

class MyAPP:
    def IntoALLAPP(driver):
        """
        先决条件：进入我家页面
        :return:
        """
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/all_application_tv").click()
        #点击全部应用，进入到我的应用


    def MyApplication(driver, AppName, wojia = False):
        """
        先决条件：进入我家页面
        从我家页面进入需要带参数 wojia = True 这样取的activity就是我家页面的activity
        :return: None
        """
        if wojia == True:
            MainActivity = ".modules.main.views.activities.MainActivity"
            driver.wait_activity("%s"%MainActivity, 30)
            time.sleep(1)
        else:
            MainActivity = ".modules.usercenter.allapp.views.activitys.AllApplicationActivity"
            driver.wait_activity("%s" %MainActivity, 30)
            time.sleep(1)

        Allname = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_app_name")
        noin = ["投诉建议", "房屋报修", "访客邀请"]
        for i in Allname:
            if i.text == AppName:
                if i.text in noin:
                    i.click()
                    try:
                        Public_Page.NoHomeInThisBuilding(driver)
                    #在该小区没有认证房间
                    except:
                        Public_Page.ExitBack(driver)
                    break
                elif i.text == "智能家居":
                    Public_Page.NomalTest(driver, title = "我的网关",
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element = "com.pujitech.atsmarthome.MySipActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_base_title",
                                          TestCase = i.text
                                          )
                    break
                elif i.text == "我的购物车":
                    Public_Page.NomalTest(driver, title = i.text,
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element = ".modules.shoppingcar.views.activities.MyShoppingCarActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                          )
                    break
                elif i.text == "房间绑定":
                    Public_Page.NomalTest(driver, title = i.text,
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element = ".modules.roombind.views.activitys.RoomBindActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                          )
                    break
                elif i.text == "社区服务":
                    Public_Page.NomalTest(driver, title = i.text,
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element = ".modules.usercenter.community.views.activities.CommunityHomeActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                          )
                    break
                elif i.text == "人脸识别":
                    Public_Page.NomalTest(driver, title = i.text,
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element = ".modules.facerecognition.views.activities.RecognitionProtocolActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                          )
                    break
                elif i.text == "商家收藏":
                    Public_Page.NomalTest(driver, title = i.text,
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element = ".modules.usercenter.collection.views.activities.CollectionActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                          )
                    break
                elif i.text == "我的家书" or i.text == "我的关注" or i.text == "我的评价" or i.text == "我的帖子":
                    Public_Page.NomalTest(driver, title = i.text,
                                          MainWait_Element = "%s"%MainActivity,
                                          find_element_id = i,
                                          Wait_Element=".modules.h5.views.activitys.CommonH5Activity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                          )
                    break