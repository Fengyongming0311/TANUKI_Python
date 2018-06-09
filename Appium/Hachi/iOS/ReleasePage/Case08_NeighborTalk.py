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

class NeighborTalk:
    #进入友邻
    def IntoNeighbor(driver):
        #先点击我家按钮进入首页页面
        Public_Page.Switch_Navigation(driver, tab="友邻")

    #点击发帖
    def IntoNewTopic(driver):
        driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_right_icon").click()

    #选择发布类型
    def ChoiceSpeakType(driver, type):
        """
        点击选择发布类型
        :param type: 1.邻里分享,2.邻里互助,3.跳蚤市场
        :return: None
        """
        driver.wait_activity(".modules.neighbors.activities.NeighborSpeakActivity", 30)
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/tv_choice_speak_type").click()
        driver.wait_activity(".modules.neighbors.activities.NeighborSpeakTypeActivity", 30)
        time.sleep(2)
        alltype = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_item_title")
        for i in alltype:
            if type == 1 and i.text == "邻里分享":
                i.click()
                break
            if type == 2 and i.text == "邻里互助":
                i.click()
                break
            if type == 3 and i.text == "跳蚤市场":
                i.click()
                break




    #发帖子
    def PostNewTopic(driver, price = None, phone = None):
        if not price == None:
            driver.find_element_by_id("com.pujitech.pujiejia:id/et_business_price").send_keys(price)
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/et_business_phone").send_keys(phone)

        time.sleep(2)
        #下面是普通的输入内容
        driver.find_element_by_id("com.pujitech.pujiejia:id/et_neighbor_speak_content").send_keys("你只看到我的楼数，却没看到我的网速。你有你的回复，我有我的速度。你嘲笑我一无所有，"
                                                                                                 "不配抢楼，我可怜你总是被抢。你可以轻视我的速度，我会证明这是谁的时代。抢楼是注定孤独的旅行，"
                                                                                                  "路上总少不了吐槽和嘲笑。但那又怎样，哪怕人头到账，"
                                                                                                  "也要抢的漂亮。我是个抢楼哥，我为自己代言！！")
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/tv_right_text").click()
        #点击发布








