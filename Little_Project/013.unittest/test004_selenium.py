from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

'''
Baidu 类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式，这是一个测试案例。
'''
class Baidu(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.baidu.com/"
		self.verificationErrors = []
		#脚本运行时，错误的信息将被打印到这个列表中。
		self.accept_next_alert = True
		#是否继续接受下一个警告。
	'''
	setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和 URL 的访问放到初始化部分。
	'''


	def test_baidu(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").send_keys("selenium webdriver")
		driver.find_element_by_id("su").click()
		driver.close()
	'''
	test_baidu 中放置的就是我们的测试脚本了，这部分我们并不陌生；因为我们执行的脚本就在这里。
	'''


	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		
		except NoSuchElementException as e:
			return False

		return True

	'''
	is_element_present 函数用来查找页面元素是否存在，try...except....为 python 语言的异常捕捉。is_element_present 函数在这里用处不大，通常删除，因为判断页面元素是否存在一般都加在 testcase 中。
	'''

	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		
		except NoAlertPresentException as e:
			return False

		return True
	'''
	对弹窗异常的处理
	'''


	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
		
			else:
				alert.dismiss()
			
			return alert_text

		finally:
			self.accept_next_alert = True
	'''
	关闭警告以及对得到文本框的处理，if 判断语句前面已经多次使用，并不陌生；try....finally...为 python的异常处理。
	'''

	def tearDown(self):
		#self.driver.quit()
		self.assertEqual([], self.verificationErrors)
		#这个是难点，对前面 verificationErrors 方法获得的列表进行比较；如查 verificationErrors 的列表不为空，输出列表中的报错信息。

	'''
	tearDown 方法在每个测试方法执行后调用，这个地方做所有测试用例执行完成的清理工作，如退出
浏览器等。
	'''


if __name__ == "__main__":
	unittest.main()
	#unitest.main()函数用来测试 类中以 test 开头的测试用例