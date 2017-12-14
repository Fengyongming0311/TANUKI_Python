#coding:utf-8
__author__ = "TANUKI"
import unittest
import HTMLTestRunner
import os, time, datetime
import sys
sys.path.append("\\report")
listaa = sys.path.append("\\test_case")
#创建测试集将文件夹下面的可测试文档全部加入

def creatsuitel():
	testunit = unittest.TestSuite()

	#discover 方法定义
	discover = unittest.defaultTestLoader.discover(listaa,
		pattern = 'start_*.py',
		top_level_dir = None)
	'''
	========
	TestLoader：测试用例加载器，其包括多个加载测试用例的方法。返回一个测试套件。
	unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。
	========
	discover(start_dir，pattern='test*.py'，top_level_dir=None)
	start_dir ：要测试的模块名或测试用例目录。
	pattern='test*.py' ：表示用例文件名的匹配原则。星号“*”表示任意多个字符。
	其中test为开头字符，可以任意更换
	'''
	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print (testunit)
	return testunit



#alltestruns = creatsuitel()
#所有测试用例集

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#取当前时间
#filename = 'D:\\selenium_python\\report\\'+now+'result.html'
filename = "report\\" + now + "result.html"
fp = open(filename, 'wb')
#定义报告存放路径

runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = u"百度搜索测试报告",
	description = u"用例执行情况")








