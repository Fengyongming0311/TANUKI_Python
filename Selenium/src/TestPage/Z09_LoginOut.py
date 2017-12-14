__author__ = 'TANUKI'
'''
Z09.实现登出账户
'''
#coding:utf-8
import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #引用Key包
from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
import sys
sys.path.append('../Center/')
#import start          #这个是为了读取start.py中的参数   下边是为了直接引用start.py中的类的
#from start import MainStart
#上边从start文件中引用MainStart类

class Z09_LoginOut:
    def LoginOut(driver):
        try:
            #登出
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("a[title=\"退出登录\"][href=\"/a/out\"]"))#wait
            driver.find_element_by_css_selector("a[title=\"退出登录\"][href=\"/a/out\"]").click()
            ## <a href="/a/out" title="退出登录"><div class="nav_left">退出</div></a>
            #<a href="/a/out" title="退出登录"><div class="nav_left">退出</div></a>

        except Exception as e:
            print ("LoginOut运行报错，报错信息为：",e)

        finally:
            pass
