__author__ = 'TANUKI'
#coding:utf-8
import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #引用Key包
from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
import sys
sys.path.append('../Center/')
import start          #这个是为了读取start.py中的参数   下边是为了直接引用start.py中的类的
#from start import MainStart
#上边从start文件中引用MainStart类


class P01_eshangjiaLoginPage:

    def LoginPage(driver):
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("username"))#wait
            driver.find_element_by_id("username").send_keys(start.username)
            #用户名输入
            #<input name="username" id="username" maxlength="30" class="login_m_but_icon" style="width:185px; height:28px; background:url(/ehomebusiness/static/images/adm.png) 15px center no-repeat; padding-left:36px; border:none; text-align:left; color:#8c9093;" placeholder="请输入用户名" autocomplete="off" type="text">

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("password"))#wait
            driver.find_element_by_id("password").send_keys(start.passwd)
            #<input id="password" name="password" maxlength="30" style="width:185px; height:28px; background:url(/ehomebusiness/static/images/passworld.png) 15px center no-repeat; padding-left:36px; border:none; text-align:left; color:#8c9093;" placeholder="请输入密码" autocomplete="off" type="password">


            """
            点击看不清操作
            """
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/form/div[2]/div[5]/a"))#wait
            driver.find_element_by_xpath("/html/body/form/div[2]/div[5]/a").click()
            #<a href="javascript:" onclick="$('.validateCode').attr('src','/ehomebusiness/servlet/validateCodeServlet?'+new Date().getTime());" class="mid validateCodeRefresh" style="">看不清</a>


            #输入验证码
            yanzhengma = input("请输入验证码...:")
            print ("输入的验证码为",yanzhengma)
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("validateCode"))#wait
            driver.find_element_by_id("validateCode").send_keys(yanzhengma)
            #<input id="validateCode" name="validateCode" placeholder="验证码" maxlength="5" class="txt required" style="width:75px; height:26px; background:url(/ehomebusiness/static/images/code.png) 15px center no-repeat; padding-left:36px; color:#8c9093; float:left;border-radius:5px; display:inline-block;margin-bottom:0;" type="text">


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[type=\"submit\"]"))#wait
            driver.find_element_by_css_selector("input[type=\"submit\"]").click()
            #<input name="" value="" style="width: 232px;height: 41px;border:0px;background:none;" type="submit">

        except Exception as e:
            print ("登录用户运行报错，报错信息为：",e)

        finally:
            pass


