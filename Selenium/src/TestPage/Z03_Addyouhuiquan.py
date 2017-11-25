__author__ = 'TANUKI'
'''
Z03.实现添加优惠券
'''
#coding:utf-8
import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #引用Key包
from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
import sys
sys.path.append('../Center/')
class Z03_Addyouhuiquan:
    def Addyouhuiquan(driver):
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[class=\"accordion-toggle\"]"))
            driver.find_element_by_css_selector("span[class=\"ehomeicon ehomeicon-yunying\"]").click()
            #<span class="ehomeicon ehomeicon-yunying"></span>
            #点击左侧树形结构运营管理

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[data-href=\".menu3-4c9a4bad3e5f475a871e3c3ac2df15a8\"]"))
            driver.find_element_by_css_selector("a[data-href=\".menu3-4c9a4bad3e5f475a871e3c3ac2df15a8\"]").click()
            #<a data-href=".menu3-4c9a4bad3e5f475a871e3c3ac2df15a8" href="/a/operation/couponManage" target="mainFrame">优惠券管理<i class="fa fa-caret-left"></i></a>
            #点击进入优惠券管理页面

            time.sleep(1)
            driver.switch_to_frame('mainFrame')   #进入主框架
            #切换到主框架

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[href=\"/a/operation/couponManage/form\"]"))
            driver.find_element_by_css_selector("a[href=\"/a/operation/couponManage/form\"]").click()
            #<a class="btn btn-primary" href="/a/operation/couponManage/form"><i class="icon-plus icon-custom"></i> 添加</a>
            #添加优惠券

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("span[class=\"select2-chosen\"]"))
            driver.find_element_by_css_selector("span[class=\"select2-chosen\"]").click()
            #<span class="select2-chosen">全部省份</span>
            #选择楼盘

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[2]/ul/li[2]"))
            driver.find_element_by_xpath("/html/body/div[2]/ul/li[2]").click()
            #选择广东

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/form/div[1]/div/div[2]/a/span[1]"))
            driver.find_element_by_xpath("/html/body/form/div[1]/div/div[2]/a/span[1]").click()
            #/html/body/form/div[1]/div/div[2]/a/span[1]

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[3]/ul/li[2]"))
            driver.find_element_by_xpath("/html/body/div[3]/ul/li[2]").click()
            #选择中山

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/form/div[1]/div/div[4]/a/span[1]"))
            driver.find_element_by_xpath("/html/body/form/div[1]/div/div[4]/a/span[1]").click()
            #/html/body/form/div[1]/div/div[4]/a/span[1]


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[4]/ul/li[2]/div"))
            driver.find_element_by_xpath("/html/body/div[4]/ul/li[2]/div").click()
            #/html/body/div[4]/ul/li[2]/div   pass
            #/html/body/div[4]/ul/li[2]
            #/html/body/div[4]/ul/li[2]/div/span
            #中山璟湖城

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("couponName"))
            driver.find_element_by_id("couponName").send_keys("普及科技4折券")
            #<input id="couponName" name="couponName" class="input-xlarge " value="" maxlength="64" type="text">
            #优惠券名称

            #case2:折扣券
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("couponType2"))
            driver.find_element_by_id("couponType2").click()
            #<input id="couponType2" name="couponType" onclick="showCouponMoneyUnit()" value="1" type="radio">

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("couponMoney2"))
            driver.find_element_by_id("couponMoney2").send_keys("40")
            #<input id="couponMoney2" name="couponMoney" class="input-medium " min="0" type="text">

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("useRule1"))
            driver.find_element_by_id("useRule1").click()
            #<input id="useRule1" name="useRule" onclick="showFullUseMoney()" value="0" type="radio">
            #使用条件无限制

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("grantType1"))
            driver.find_element_by_id("grantType1").click()
            #<input id="grantType1" name="grantType" onclick="showLimitedNum()" value="0" type="radio">
            #发放总量

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("useScope1"))
            driver.find_element_by_id("useScope1").click()
            #<input id="useScope1" name="useScope" onclick="showUserObject()" value="0" type="radio">
            #使用范围

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("shareFlag1"))
            driver.find_element_by_id("shareFlag1").click()
            #<input id="shareFlag1" name="shareFlag" value="1" type="radio">
            #优惠同享


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("validityType2"))
            driver.find_element_by_id("validityType2").click()
            #<input id="validityType2" name="validityType" onclick="showValidityType()" value="1" type="radio">
            #有效期

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("validityDays"))
            driver.find_element_by_id("validityDays").send_keys("365")
            #<input id="validityDays" name="validityDays" min="0" class="input-medium" value="0" maxlength="11" type="text">
            #XXX天内有效


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("receiveType1"))
            driver.find_element_by_id("receiveType1").click()
            #<input id="receiveType1" name="receiveType" onclick="showReceiveType()" value="0" type="radio">
            #领取方式

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("receiveRule1"))
            driver.find_element_by_id("receiveRule1").click()
            #<input id="receiveRule1" name="receiveRule" value="0" type="radio">
            #无限制领取

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("activeStartTime"))
            driver.find_element_by_id("activeStartTime").click()
            #<input id="activeStartTime" name="activeStartTime" readonly="readonly" maxlength="20" class="input-medium Wdate" value="" onclick="WdatePicker({dateFmt:'yyyy-MM-dd HH:mm:ss',minDate:'%y-%M-%d',maxDate:'#F{$dp.$D(\'activeEndTime\')}', alwaysUseStartDate:true,isShowClear:true});" type="text">
            #活动起始时间

            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[2]/iframe"))
            '''
            case3：
            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame('iFrame')

            case2:
            driver.switch_to_frame('iFrame')

            case1：
            time.sleep(3)
            shijian = driver.find_element_by_xpath("/html/body/div[2]/iframe")
            driver.switch_to_frame(shijian)
            #切换到时间iframe
            #/html/body/div[2]/iframe
            #<iframe hidefocus="true" border="0" scrolling="no" style="width: 202px; height: 243px;" height="9" frameborder="0" width="97"></iframe>
            #<iframe hidefocus="true" border="0" scrolling="no" style="width: 202px; height: 243px;" height="9" frameborder="0" width="97"></iframe>

            '''



            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[id=\"dpTodayInput\"][value=\"今天\"]"))
            driver.find_element_by_css_selector("input[id=\"dpTodayInput\"][value=\"今天\"]").click()
            '''
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("dpTodayInput"))
            driver.find_element_by_id("dpTodayInput").click()
            '''
            #<input class="dpButton" id="dpTodayInput" value="今天" type="button">
            #选择今天

            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame('mainFrame')   #进入主框架

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("activeEndTime"))
            driver.find_element_by_id("activeEndTime").click()
            #<input id="activeEndTime" name="activeEndTime" readonly="readonly" maxlength="20" class="input-medium Wdate compareActiveTime" value="" onclick="WdatePicker({dateFmt:'yyyy-MM-dd HH:mm:ss',minDate:'#F{$dp.$D(\'activeStartTime\')}', alwaysUseStartDate:true,isShowClear:true});" type="text">
            #活动结束时间

            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[2]/iframe"))


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("dpTodayInput"))
            driver.find_element_by_id("dpTodayInput").click()
            #<input class="dpButton" id="dpTodayInput" value="今天" type="button">
            #选择今天

            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame('mainFrame')   #进入主框架


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("btnSubmit"))
            driver.find_element_by_id("btnSubmit").click()
            #<input id="btnSubmit" class="btn btn-primary" value="保 存" type="submit">
            #保存

            UnitResult = True
            #下返回测试结果
            return (UnitResult)

        except Exception as e:
            print ("添加优惠券报错，报错信息为：",e)
            UnitResult = False
            #下返回测试结果
            return (UnitResult)
        finally:
            pass
