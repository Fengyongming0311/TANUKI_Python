# /usr/bin/python
# encoding: utf-8

from widget import Widget  
import unittest  

#执行测试的类  
class WidgetTestCase(unittest.TestCase):  
    def setUp(self):  
        self.widget = Widget()  

    def tearDown(self):  
        self.widget.dispose()  
        self.widget = None  

    def test_size(self):  
        self.assertEqual(self.widget.getSize(), (40, 40))  

    def test_resize(self):  
        self.widget.resize(100, 100)  
        self.assertEqual(self.widget.getSize(), (100, 100))  

#测试  
if __name__ == "__main__":  
    #构造测试集              
    suite = unittest.TestSuite()  
    suite.addTest(WidgetTestCase("test_size"))  
    suite.addTest(WidgetTestCase("test_resize"))  
    #执行测试  
    runner = unittest.TextTestRunner()  
    runner.run(suite)


'''
编写测试用例（TestCase）并将它们组织成测试用例集（TestSuite）的最终目的只有一个：实施测试并获得最终结果。PyUnit使用TestRunner类作为测试用例的基本执行环境，来驱动整个单元测试过程。但是Python开发人员在进行单元测试时一般不直接使用TestRunner类，而是使用其子类TextTestRunner来完成测试，并将测试结果以文本方式显示出来。举例说明如下：
'''