# _*_ coding:utf-8 _*_
__author__ = '苦叶子'

import unittest
import sys
from imp import reload
reload(sys)


class suiteTest(unittest.TestCase):
	def setUp(self):
		self.a = 10
		self.b = 20

	def testadd(self):
		# 验证加法
		result = self.a + self.b
		self.assertTrue(result == 100)

	def testsub(self):
		# 验证减法
		result = self.a - self.b
		self.assertTrue(result == -10)


#定义suite
def suite():
	suite = unittest.TestSuite()
	
	#添加测试方法
	suite.addTest(suiteTest("testadd"))
	suite.addTest(suiteTest("testsub"))

	## 或用以下方式添加测试方法
	#suite.addTest(unittest.makeSuite(suiteTest))
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	test_suite = suite()
	runner.run(test_suite)