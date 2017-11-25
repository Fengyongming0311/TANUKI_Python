#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner

class Baidu(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.baidu.com/"
		self.verificationErrors = []
		self.accept_next_alert = True


	#百度搜索用例
	def test_baidu_search(self):
		"""百度搜索"""
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").send_keys("selenium webdriver")
		driver.find_element_by_id("su").click()
		time.sleep(2)
		driver.close()

	#百度设置用例
	def test_baidu_set(self):
		"""百度设置"""
		driver = self.driver
		#进入搜索设置页
		driver.get(self.base_url + "/gaoji/preferences.html")
		#设置每页搜索结果为 50 条
		m=driver.find_element_by_name("NR")
		m.find_element_by_xpath("//option[@value='50']").click()
		time.sleep(2)
		driver.close()

		#保存设置的信息
		#driver.find_element_by_xpath("//input[@value='保存设置']").click()
		#time.sleep(2)
		#driver.switch_to_alert().accept()
		

	def tearDown(self):
		#self.driver.close()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	testunit = unittest.TestSuite()
	#定义一个单元测试容器

	testunit.addTest(Baidu("test_baidu_search"))
	testunit.addTest(Baidu("test_baidu_set"))
	#添加测试用例

	now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
	#取当前时间

	filename = now + "result.html"
	fp = open(filename, 'wb')
	#定义报告存放路径

	runner = HTMLTestRunner.HTMLTestRunner(
		stream = fp,
		title = u"百度搜索测试报告",
		description = u"用例执行情况")


	#运行测试用例
	runner.run(testunit)
