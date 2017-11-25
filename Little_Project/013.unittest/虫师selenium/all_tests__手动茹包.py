#coding=utf-8
import unittest
#这里需要导入测试文件
import sys
sys.path.append("\\test_case")
from test_case import youdao
from test_case import baidu
import HTMLTestRunner
import time

testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

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