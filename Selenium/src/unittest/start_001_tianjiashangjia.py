##coding=utf-8
__author__ = 'TANUKI'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
###
import sys
sys.path.append('../Center/')
import start          #这个是为了读取start.py中的参数   下边是为了直接引用start.py中的类的
###
sys.path.append('../TestPage/')
from Z01_LoginPage import Z01_LoginPage
from Z02_Addshangjia import Z02_Addshangjia
###
"""
self.assertEqual([], self.verificationErrors) 是个难点，对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，
输出列表中的报错信息。
而且，这个东西，也可以将来被你自己更好的调用和使用，根据自己的需要写入你希望的信息。（rabbit 告诉我的）
"""

class Addshangjia(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = start.login_url
		self.verificationErrors = []
		self.accept_next_alert = True

	#添加商家测试用例
	def test_addshangjia(self):
		"""用例名称:智慧社区添加商家信息"""
		driver = self.driver
		driver.get(self.base_url + "/")
		Z01_LoginPage.LoginPage(driver)
		self.assertEqual(driver.title, "智慧社区综合管理平台")
		UnitResult = Z02_Addshangjia.Addshangjia(driver)
		self.assertTrue(UnitResult)
		#判断测试结果



	def tearDown(self):
		self.driver.close()
		self.assertEqual([], self.verificationErrors)




if __name__ == "__main__":
	unittest.main()