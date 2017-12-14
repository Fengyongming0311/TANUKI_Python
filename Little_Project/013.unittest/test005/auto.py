#coding= utf-8
from widget import Widget
import unittest

# 执行测试的类
class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = Widget()
	
	def testSize(self):
		self.assertEqual(self.widget.getSize(), (40, 40))

	#新加的测试widget.py中resize()方法的测试用例
	def testResize(self):
		self.widget.resize(100, 100)
		self.assertEqual(self.widget.getSize(), (100, 100))

	def testmycase(self):
		self.widget.resize(10,100)
		self.assertEqual(self.widget.getSize(), (10,100))


	def tearDown(self):
		self.widget.dispose()
		self.widget = None


# 构造测试集
def suite():
	suite = unittest.TestSuite()
	suite.addTest(WidgetTestCase("testSize"))
	suite.addTest(WidgetTestCase("testResize"))
	#新增testresize
	suite.addTest(WidgetTestCase("testmycase"))
	return suite

#执行测试
if __name__ == "__main__":
	unittest.main(defaultTest = 'suite')


'''
if __name__ == "__main__":解释
顾名思义，if 就是如果的意思，在句子开始处加上 if，就说明，这个句子是一个条件语句。接着是
__name__，__name__作为模块的内置属性，简单点说呢，就是.py 文件的调用方式。最后是__main__，刚
才我也提过，.py 文件有两种使用方式：作为模块被调用和直接使用。如果它等于"__main__"就表示是直接
执行。
'''