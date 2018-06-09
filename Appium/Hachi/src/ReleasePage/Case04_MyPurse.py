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

class MyPurse:
    def IntoPurse(driver):
        """
        先决条件：进入我家页面
        :return: None
        """
        #测试点击我的钱包进入我的钱包页面
        Public_Page.NomalTest(driver, title = "我的钱包",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/tv_user_wallet",
                              Wait_Element = ".modules.wallet.views.activitys.MyWalletActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title")

        #测试点击我的钱包额度进入我的钱包页面
        Public_Page.NomalTest(driver, title = "我的钱包",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/tv_wallet",
                              Wait_Element = ".modules.wallet.views.activitys.MyWalletActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title",
                              YESBack = False)

        #点击余额说明
        Public_Page.NomalTest(driver, title = "余额说明",
                              MainWait_Element = ".modules.wallet.views.activitys.MyWalletActivity",
                              find_element_id = "com.pujitech.pujiejia:id/my_wallet_yue_shuoming_tv",
                              Wait_Element = ".modules.help.view.activities.HelpActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title")


        #点击去充值
        Public_Page.NomalTest(driver, title = "余额充值",
                              MainWait_Element = ".modules.wallet.views.activitys.MyWalletActivity",
                              find_element_id = "com.pujitech.pujiejia:id/my_wallet_qu_chongzhi_btn",
                              Wait_Element = ".modules.wallet.views.activitys.MyWalletYuEChongzhiActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title")

        # 下滑查看余额明细
        driver.wait_activity(".modules.wallet.views.activitys.MyWalletActivity", 30)
        time.sleep(2)
        driver.swipe(500, 1700, 500, 1000)
        time.sleep(2)
        driver.swipe(500, 1700, 500, 1000)

        #点击更多明细(并下滑查看数据)
        Public_Page.NomalTest(driver, title = "更多明细",
                              MainWait_Element = ".modules.wallet.views.activitys.MyWalletActivity",
                              find_element_id = "com.pujitech.pujiejia:id/my_wallet_more_mingxi_tv",
                              Wait_Element = ".modules.wallet.views.activitys.MyWalletMoreMingxiActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title",
                              YESBack = False)

        huadong.shanghua(driver, 1000)
        time.sleep(3)
        huadong.shanghua(driver, 1000)
        time.sleep(3)
        huadong.shanghua(driver, 1000)
        time.sleep(3)
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
        #退回到我的钱包页面
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
        #再次点击退回到我家页面
