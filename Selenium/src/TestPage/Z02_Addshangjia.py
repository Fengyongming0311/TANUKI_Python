__author__ = 'TANUKI'
'''
Z02.实现添加商家信息
'''
#coding:utf-8
import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #引用Key包
from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
import sys
import start
sys.path.append('../Center/')
sys.path.append('../Picture/')

class Z02_Addshangjia:
    def Addshangjia(driver):
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("span[class=\"ehomeicon ehomeicon-shop\"]"))
            driver.find_element_by_css_selector("span[class=\"ehomeicon ehomeicon-shop\"]").click()
            #点击左侧树形结构商家管理
            #<span class="ehomeicon ehomeicon-shop"></span>
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[data-href=\".menu3-20bad7d9f47e43f7b8f1417da8c23fb0\"]"))
            driver.find_element_by_css_selector("a[data-href=\".menu3-20bad7d9f47e43f7b8f1417da8c23fb0\"]").click()
            #点击商家信息进入商家信息页面
            #<a data-href=".menu3-20bad7d9f47e43f7b8f1417da8c23fb0" href="/a/business/businessInfo" target="mainFrame">商家信息<i class="fa fa-caret-left"></i></a>

            time.sleep(1)
            #driver.switch_to_default_content()    #退出框架
            driver.switch_to_frame('mainFrame')   #进入主框架
            #切换到主框架
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[class=\"btn btn-primary\"]"))
            driver.find_element_by_css_selector("a[class=\"btn btn-primary\"]").click()
            #<a class="btn btn-primary" href="/a/business/businessInfo/edit"><i class="icon-plus icon-custom"></i> 添加</a>
            #点击添加按钮
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("businessName"))
            driver.find_element_by_id("businessName").send_keys("普及科技10")
            #<input id="businessName" name="businessName" class="input-xlarge required" value="" maxlength="64" type="text">
            #输入商家名称

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("file"))
            driver.find_element_by_id("file").send_keys(start.tupianpath)
            #<input name="file" id="file" class="file" value="" accept="image/jpg,image/jpeg,image/png,image/bmp" imgheight="563" imgwidth="750" type="file">
            #上传图片

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("contactPerson"))
            driver.find_element_by_id("contactPerson").send_keys("周比利")
            #<input id="contactPerson" name="contactPerson" class="input-xlarge required" value="" maxlength="64" type="text">
            #联系人

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("phoneNum"))
            driver.find_element_by_id("phoneNum").send_keys("13258951753")
            #<input id="phoneNum" name="phoneNum" class="input-xlarge required" value="" maxlength="64" type="text">
            #联系电话

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[name=\"categoryIdList\"][value=\"02\"]"))
            driver.find_element_by_css_selector("input[name=\"categoryIdList\"][value=\"02\"]").click()
            #<input name="categoryIdList" pattren="0" value="02" type="checkbox">
            #商家分类

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[class=\"select2-choice\"]"))
            driver.find_element_by_css_selector("a[class=\"select2-choice\"]").click()
            #<a href="javascript:void(0)" onclick="return false;" class="select2-choice" tabindex="-1">   <span class="select2-chosen">全部省份</span><abbr class="select2-search-choice-close"></abbr>   <span class="select2-arrow"><b></b></span></a>
            #城市

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[2]/ul/li[2]/div"))
            driver.find_element_by_xpath("/html/body/div[2]/ul/li[2]/div").click()
            #选择广东

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/a"))
            driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/a").click()
            #/html/body/form/div[6]/div/div[1]/a
            #/html/body/form/div[6]/div/div[2]/a
            #/html/body/form/div[6]/div/div[2]/a
            #/html/body/form/div[6]/div/div[3]/a

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[3]/ul/li[3]/div"))
            driver.find_element_by_xpath("/html/body/div[3]/ul/li[3]/div").click()
            #城市选广州


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/form/div[6]/div/div[3]/a"))
            driver.find_element_by_xpath("/html/body/form/div[6]/div/div[3]/a").click()

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[4]/ul/li[4]/div"))
            driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]/div").click()
            #荔湾区


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("addrDetail"))
            driver.find_element_by_id("addrDetail").send_keys("中山八路与荔湾路的交汇处是一所综合性医院")
            #<input id="addrDetail" name="addrDetail" placeholder="详细地址" class="input-xlarge required" value="" maxlength="200" type="text">
            # #中山八路与荔湾路的交汇处是一所综合性医院

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("businessLabel"))
            driver.find_element_by_id("businessLabel").send_keys("富力地产,实地地产")
            #<input id="businessLabel" name="businessLabel" class="input-xlarge required" value="" maxlength="128" type="text">
            #商家标签:富力地产,实地地产

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("businessHours"))
            driver.find_element_by_id("businessHours").send_keys("24H")
            #<input id="businessHours" name="businessHours" class="input-xlarge" value="" maxlength="20" type="text">
            #营业时间

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"3002\"]"))
            driver.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"3002\"]").click()
            #<input name="villageIdList" value="3002" type="checkbox">
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"2801\"]"))
            driver.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"2801\"]").click()
            # <input name="villageIdList" value="2801" type="checkbox">
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"3201\"]"))
            driver.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"3201\"]").click()
            #<input name="villageIdList" value="3201" type="checkbox">
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"2401\"]"))
            driver.find_element_by_css_selector("input[name=\"villageIdList\"][value=\"2401\"]").click()
            #<input name="villageIdList" value="2401" type="checkbox">
            #服务范围



            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("groupPurchaseFlag1"))
            driver.find_element_by_id("groupPurchaseFlag1").click()
            #<input id="groupPurchaseFlag1" name="groupPurchaseFlag" class="required" value="1" type="radio">
            #选择是否支持团购

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("rate"))
            driver.find_element_by_id("rate").send_keys("6")
            #<input id="rate" name="rate" class="input-mini required number" maxlength="10" type="text">
            #每笔订单收取订单金额



            #<a href="javascript:void(0)" onclick="return false;" class="select2-choice" tabindex="-1">   <span class="select2-chosen"></span><abbr class="select2-search-choice-close"></abbr>   <span class="select2-arrow"><b></b></span></a>
            #<div id="s2id_balanceCycle" class="select2-container input-medium required number">
            # #结算周期
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/form/div[16]/div/div/a"))
            driver.find_element_by_xpath("/html/body/form/div[16]/div/div/a").click()



            #case2:<div class="select2-result-label"> CSS定位
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("div[class=\"select2-result-label\"]"))
            driver.find_element_by_css_selector("div[class=\"select2-result-label\"]").click()
            #我操！！！没想到卡了我一下午的问题让我用case2就解决了....666666666666666666666



            '''
            #case1:打开弹框后用Xpath定位
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[2]/ul/li[1]"))
            driver.find_element_by_xpath("/html/body/div[2]/ul/li[1]").click()
            '''

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("distributeModel2"))
            driver.find_element_by_id("distributeModel2").click()
            #<input id="distributeModel2" name="distributeModel" value="1" type="radio">
            #选第三方配送

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("btnSubmit"))
            driver.find_element_by_id("btnSubmit").click()
            #<input id="btnSubmit" class="btn btn-success" value="保 存" type="submit">
            #点击保存

            UnitResult = True
            #下返回测试结果
            return (UnitResult)


        except Exception as e:
            print ("添加商户运行报错，报错信息为：",e)
            UnitResult = False
            #下返回测试结果
            return (UnitResult)

        finally:
            pass
