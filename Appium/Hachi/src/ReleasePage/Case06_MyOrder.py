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

class MyOrder:
    def WoJiaOrder(driver):
        """
        先决条件：进入我家页面
        :return: None
        """
        time.sleep(3)
        orderNo = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_order_number")[0]
        print (orderNo)
        print (orderNo.text)
        if "订单号" not in orderNo.text:
            pass
        else:
            Public_Page.NomalTest(driver, title = "订单详情",
                                  MainWait_Element = ".modules.main.views.activities.MainActivity",
                                  find_element_id = orderNo,
                                  Wait_Element = ".modules.usercenter.order.views.activities.OrderDetailsActivity",
                                  check_element_id = "com.pujitech.pujiejia:id/tv_title"
                                  )


    def AllOrder(driver):
        """
        先决条件: 进入我家页面
        :return: None
        """
        time.sleep(2)
        #点击全部订单进入我的订单页面
        Public_Page.NomalTest(driver, title = "我的订单",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/ll_all_order_container",
                              Wait_Element = ".modules.usercenter.order.views.activities.OrderListActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title",
                              YESBack = False)

    def ClickMyOrder(driver):
        """
        进入我的订单页面，脚本执行完成后返回我家页面
        :return: None
        """
        """
        订单状态：配送中  待自提  已完成  已退款  已取消  待支付  待受理  已受理  
        """
        orderstatus = ['配送中', '待自提', '已完成', '已退款', '已取消', '待支付', '待受理', '已受理']
        for status in orderstatus:
            time.sleep(2)
            order = driver.find_elements_by_id("com.pujitech.pujiejia:id/order_state")
            for i in order:
                if i.text == status:
                    Public_Page.NomalTest(driver, title = "订单详情",
                                          MainWait_Element = ".modules.usercenter.order.views.activities.OrderListActivity",
                                          find_element_id = i,
                                          Wait_Element = ".modules.usercenter.order.views.activities.OrderDetailsActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title",
                                          YESBack = False)

                    Public_Page.NomalTest(driver, title = "订单状态跟踪",
                                          MainWait_Element = ".modules.usercenter.order.views.activities.OrderDetailsActivity",
                                          find_element_id = "com.pujitech.pujiejia:id/tv_more_status",
                                          Wait_Element=".modules.usercenter.order.views.activities.OrderStatusActivity",
                                          check_element_id = "com.pujitech.pujiejia:id/tv_title",
                                          TestCase = status + "订单")
                    time.sleep(1)
                    driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
                    break

        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
        #返回我家页面
        '''
                orderstatus = {
                    'peisongzhong': "",
                    'daiziti': "",
                    'yiwancheng' : "",
                    'yituikuan' : "",
                    'yiquxiao' : "",
                    'daizhifu' : "",
                    'daishouli' : "",
                    'yishouli' : ""
                }
                #每个订单状态取第一个值，然后点击查看订单

                for i in order:
                    if i.text =='已完成':
                        orderstatus['yiwancheng'] = i
                        continue
                    elif i.text == '已退款':
                        orderstatus['yituikuan'] = i
                        continue
                    elif i.text == '已取消':
                        orderstatus['yiquxiao'] = i
                        continue
                    elif i.text == '待支付':
                        orderstatus['daizhifu'] = i
                        continue
                    elif i.text == '待受理':
                        orderstatus['daishouli'] = i
                        continue
                    elif i.text == '待自提':
                        orderstatus['daiziti'] = i
                        continue
                    elif i.text == '已受理':
                        orderstatus['yishouli'] = i
                        continue
                    elif i.text == '配送中':
                        orderstatus['peisongzhong'] = i
                        continue
                    else:
                        pass

                for i in order:
                    if i.text =='已完成' and orderstatus['yiwancheng'] == '':
                        orderstatus['yiwancheng'] = i
                        continue
                    elif i.text == '已退款' and orderstatus['yituikuan'] == '':
                        orderstatus['yituikuan'] = i
                        continue
                    elif i.text == '已取消' and orderstatus['yiquxiao'] == '':
                        orderstatus['yiquxiao'] = i
                        continue
                    elif i.text == '待支付' and orderstatus['daizhifu'] == '':
                        orderstatus['daizhifu'] = i
                        continue
                    elif i.text == '待受理' and orderstatus['daishouli'] == '':
                        orderstatus['daishouli'] = i
                        continue
                    elif i.text == '待自提' and orderstatus['daiziti'] == '':
                        orderstatus['daiziti'] = i
                        continue
                    elif i.text == '已受理' and orderstatus['yishouli'] == '':
                        orderstatus['yishouli'] = i
                        continue
                    elif i.text == '配送中' and orderstatus['peisongzhong'] == '':
                        orderstatus['peisongzhong'] = i
                        continue
                    else:
                        pass

                #再遍历字典中每一个值，如果有值就进行查看订单操作
                for key,value in orderstatus.items():
                    #print (key,':',value)
                    if not value == '':
                        print (key,':',value)
                        Public_Page.NomalTest(driver, title="订单详情",
                                              MainWait_Element=".modules.usercenter.order.views.activities.OrderListActivity",
                                              find_element_id = value,
                                              Wait_Element=".modules.usercenter.order.views.activities.OrderDetailsActivity",
                                              check_element_id="com.pujitech.pujiejia:id/tv_title")

                    else:
                        continue
                    time.sleep(3)
                '''


