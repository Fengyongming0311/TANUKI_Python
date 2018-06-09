__author__ = 'TANUKI'
#coding:utf-8
#生产版本的自动化测试

import sys
sys.path.append("..")
from appium import webdriver
#import os,time
from Public import testphone
#img_file = img_file.img_file()  #定义图片文件保存的位置
############导入测试用例###############
sys.path.append("../ReleasePage")
#from 文件名 import Class名
from Case01_Loginin import Loginin
from Case02_ShiDiPai import ShiDiPai
from Case03_MyHome import MyHome
from Case04_MyPurse import MyPurse
from Case05_MyCoupon import MyCoupon
from Case06_MyOrder import MyOrder
from Case07_MyAPP import MyAPP
from Case08_NeighborTalk import NeighborTalk
from FilePublic_Page import Public_Page

######################################

shouji = testphone.testphone()
#读取被测的手机型号
driver = webdriver.Remote('http://localhost:4723/wd/hub', shouji)
'''
Loginin.OnceInto(driver)
Loginin.OnceIntoLogin(driver)
Loginin.OnceChoiceBuilding(driver, Building = "哈奇内部测试")
#case:测试第一次登录
############################################################

#Loginin.Loginin_nomal(driver, 13263160105, "00000000")
#普通账号登录
#Loginin.Loginin_Switch_ID(driver, username = 13466738904, password = "00000000")
ShiDiPai.IntoShiDiPai(driver)
ShiDiPai.Building_Name_Container(driver)
Public_Page.ChoiceBuilding(driver, Building = "哈奇内部测试")
#case:切换账号并切换到哈其内部测试楼盘下
'''

#测试平时登录账户(在已有楼盘下账户未登录状态)

ShiDiPai.IntoShiDiPai(driver)
ShiDiPai.RecommendApp(driver)
ShiDiPai.Brand_Image(driver)
ShiDiPai.ZunXiangFuWu(driver)
ShiDiPai.XiaLaPage(driver)
ShiDiPai.Community_Image(driver)
ShiDiPai.Recommend_Community_Title(driver)
ShiDiPai.More_Building(driver)
###################################


MyHome.IntoMyHome(driver)
MyHome.MyHome_two(driver)
MyHome.Change_ProfilePhoto(driver)
MyHome.Change_PersonalData(driver)
MyHome.AddressManage(driver)
#MyHome.DeleteAddress(driver, 3)
#测试我家页面中各个功能
MyPurse.IntoPurse(driver)
#进入我的钱包

MyCoupon.IntoCoupon(driver)
#进入我的优惠券
MyOrder.WoJiaOrder(driver)
MyOrder.AllOrder(driver)
MyOrder.ClickMyOrder(driver)
#我的订单订单管理



MyHome.IntoMyHome(driver)
#单独测试就得重新进入我家

MyAPP.MyApplication(driver, AppName = "我的购物车", wojia = True)
MyAPP.MyApplication(driver, AppName = "房间绑定", wojia = True)
MyAPP.MyApplication(driver, AppName = "投诉建议", wojia = True)
MyAPP.MyApplication(driver, AppName = "房屋报修", wojia = True)
MyAPP.MyApplication(driver, AppName = "社区服务", wojia = True)
MyAPP.MyApplication(driver, AppName = "智能家居", wojia = True)
MyAPP.MyApplication(driver, AppName = "人脸识别", wojia = True)
MyAPP.MyApplication(driver, AppName = "访客邀请", wojia = True)
#我家的我的应用（从我家页面进入需要带参数wojia = True）

MyAPP.IntoALLAPP(driver)
#点击全部应用进入全部应用
MyAPP.MyApplication(driver, AppName = "商家收藏")
MyAPP.MyApplication(driver, AppName = "我的家书")
MyAPP.MyApplication(driver, AppName = "我的关注")
MyAPP.MyApplication(driver, AppName = "我的评价")
MyAPP.MyApplication(driver, AppName = "我的帖子")
Public_Page.ExitBack(driver)
#返回到我家页面
MyHome.SmartBandInstruction(driver)

NeighborTalk.IntoNeighbor(driver)
#进入友邻页面
NeighborTalk.IntoNewTopic(driver)
NeighborTalk.ChoiceSpeakType(driver, type = 3)
NeighborTalk.PostNewTopic(driver, price = 100, phone = 13435951753)
