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

class MyCoupon:
    def IntoCoupon(driver):
        """
        先决条件：进入我家页面
        :return: None
        """

        #测试点击我的优惠券进入我的优惠券页面
        Public_Page.NomalTest(driver, title = "我的优惠券",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/rl_user_coupon_container",
                              Wait_Element = ".modules.usercenter.coupon.view.activities.AvailableCouponActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title",
                              YESBack = False)

        #点击优惠券使用说明
        Public_Page.NomalTest(driver, title="使用说明",
                              MainWait_Element=".modules.usercenter.coupon.view.activities.AvailableCouponActivity",
                              find_element_id="com.pujitech.pujiejia:id/tv_coupon_top",
                              Wait_Element=".modules.help.view.activities.HelpActivity",
                              check_element_id="com.pujitech.pujiejia:id/tv_title",
                              )
        #查看无效优惠券
        Public_Page.NomalTest(driver, title="无效优惠券",
                              MainWait_Element=".modules.usercenter.coupon.view.activities.AvailableCouponActivity",
                              find_element_id="com.pujitech.pujiejia:id/tv_bottom_coupon",
                              Wait_Element=".modules.usercenter.coupon.view.activities.UnAvailableCouponActivity",
                              check_element_id="com.pujitech.pujiejia:id/tv_title",
                              )


        time.sleep(3)
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
        #退回到我家页面
