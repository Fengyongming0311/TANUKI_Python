__author__ = 'TANUKI'
#coding:utf-8
import os,time
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
import sys
sys.path.append('../Center/')
import start


class P02_insertfuwufenlei:
    #功能代码
    def Insertfuwufenlei(driver):
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a"))#wait
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a").click()
        #<a class="accordion-toggle" data-toggle="collapse" data-parent="#menu-eb707ad7c84e48a29504d1ce5ddb2abe" data-href="#collapse-c52b9653277947e8abac6b0f5ca33622" href="#collapse-c52b9653277947e8abac6b0f5ca33622" title="">


        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/ul/li[2]/a"))#wait
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/ul/li[2]/a").click()

        time.sleep(1)
        driver.switch_to_default_content()    #退出框架
        time.sleep(1)
        #driver.switch_to_frame('mainFrame')   #进入主框架
        #这里要切换iframe
        #/html/body/div[1]/div[2]/div[1]/div[3]/iframe
        #<iframe id="mainFrame" name="mainFrame" src="" style="overflow: visible; height: 392px; display:
        driver.switch_to_frame('jerichotabiframe_1')   #进入主框架
        #下面还有一个iframe
        #<iframe id="jerichotabiframe_1" name="jerichotabiframe_1" src="/ehomebusiness/a/service/serviceSortInfo?tabPageId=jerichotabiframe_1" scrolling="auto" style="width: 100%; height: 361px; border: 0px none;" frameborder="0">
        print ("001fengyongming")


        #WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("name"))#wait
        driver.find_element_by_id("name").send_keys("北京同仁堂1")
        #<input id="name" class="input-xlarge" name="name" placeholder="请输入分类名称" value="" maxlength="6" type="text">
        #输入名称

        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[id=\"sortOrder\"][name=\"sortOrder\"]"))#wait
        driver.find_element_by_css_selector("input[id=\"sortOrder\"][name=\"sortOrder\"]").send_keys("001")
        #<input id="sortOrder" class="input-xlarge number" name="sortOrder" placeholder="请输入排序号" value="" maxlength="3" type="text">
        #输入排序

        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[id=\"btnSubmit\"][type=\"submit\"]"))#wait
        driver.find_element_by_css_selector("input[id=\"btnSubmit\"][type=\"submit\"]").click()
        #<input id="btnSubmit" class="btn btn-success" value="保存分类" type="submit">
        #点击保存分类