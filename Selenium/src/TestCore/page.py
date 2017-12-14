__author__ = 'TANUKI'
#coding:utf-8

import os,time
import read_cfg      #读取我自己写的配置文件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #引用Key包
from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包



#创建整体模块大类
class Page():
    #调用火狐浏览器模块
    def create_Firefox(self):
        driver = webdriver.Firefox()
        #打开火狐浏览器

        return driver
    #获取url
    def geturl(self, url):
        driver.get(url)
        time.sleep(1)


    #find_element_by_css_selector简化
    def findcss(self):




