__author__ = "TANUKI"
'''
整合有个问题，那就是程序整体执行完之后才完成报告文件的写入，不好使，分成两个文件执行
'''
#coding:utf-8
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
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



alltestruns = creatsuitel()
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




def send_email(file_new):

    #发送邮箱服务器
    smtpserver = 'smtp.sohu.com'
    #发送邮箱用户名/密码
    user = 'fengyongming0311'
    password = '1qaz2wsx'
    #发送邮箱
    sender = 'fengyongming0311@sohu.com'
    #多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['342469367@qq.com','fengyongming@pujitech.com','fengyongming0311@sohu.com']
    #发送邮件主题
    subject = now + '执行自动化测试报告邮件'
    mailfrom = now + '自动化测试结果邮件<fengyongming0311@sohu.com>'
    #这里填写邮件发送自XXXXXXXXXXXXXXXX

    msg = MIMEMultipart('mixed')
    #混合型邮件类型，包括纯文本和html，图片声音等

    '''
    这里是发送邮件的内容
    '''
    #定义正文这里修改
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    #print ("信件内容为：===================>", mail_body)

    msg = MIMEText(mail_body, 'html', 'utf-8')
    #text_plain = MIMEText(text,'plain', 'utf-8')
    #msg.attach(text_plain)


    msg['Subject'] = Header(subject,'utf-8')
    #标题格式
    msg['From'] = mailfrom
    #发送自....格式
    msg['To'] = ";".join(receiver)
    #发送给XXX，多人的格式
    #msg['To'] = 'XXX@126.com'
    #发送给XXX，单个收件人的格式
    msg['Date'] = getTime()
    #发送时间
    #要在163有限（邮箱？？）设置授权码（即客户端的密码），否则会报535

    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print ("邮件已经发送完毕！！")
    print ("====================程序结束====================")

def sendreport():
	result_dir = "report\\"
	lists = os.listdir(result_dir)

	lists.sort(key = lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
	#上句为了找出最新的文件

	#print (u"最新测试生成的报告为：" + lists[-1])
	#找到最新生成的文件
	file_new = os.path.join(result_dir, lists[-1])

	print ("发送的HTML文件名称为：============>", file_new)


	send_email(file_new)
	#调用发邮件模块,把找到的文件传入send_email方法中


def getTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))







if __name__ == '__main__':
	runner.run(alltestruns)
	#执行测试用例
	time.sleep(3)
	fp.close()
	#跑完脚本等待３秒把报告文件关闭然后发送邮件
	sendreport()
	#执行发邮件