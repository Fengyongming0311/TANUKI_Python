__author__ = 'TANUKI'
#coding:utf-8
import time
###
import sys
sys.path.append("..")
from FilePublic_Page import Public_Page
from Case01_Loginin import Loginin
import huadong
import random
###
class TestDondake:
    def FYMtest(driver):
        Public_Page.Switch_Navigation(driver, tab= "实地派")
        time.sleep(1)

        #Public_Page.RandomBuilding(driver)
        Public_Page.ChoiceBuilding(driver, Building = "常春藤")
        time.sleep(2)

        Loginin.Loginin_nomal(driver)

        time.sleep(2)

        allapp = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_app_name")

        for i in allapp:
            if i.text == "房间绑定":
                fangjianbangding = i
                break

        Public_Page.NomalTest(driver, title="房间绑定",
                              MainWait_Element=".modules.main.views.activities.MainActivity",
                              find_element_id= fangjianbangding,
                              Wait_Element=".modules.roombind.views.activitys.RoomBindActivity",
                              check_element_id="com.pujitech.pujiejia:id/tv_title"
                              )

        Public_Page.Dengchu(driver)



