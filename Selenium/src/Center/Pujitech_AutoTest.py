#coding:utf-8
__author__ = 'TANUKI'
#测试脚本总流程执行开始文件
import unittest
import HTMLTestReportCN
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import os, time, datetime
import sys
sys.path.append("../Report/")
#测试报告存放路径
sys.path.append("../unittest/")
listaa = os.chdir("../unittest/")
#unittest测试脚本存放路径,在不同的文件夹下需要切换目录...

def creatsuitel():
	testunit = unittest.TestSuite()
	#discover 方法定义
	discover = unittest.defaultTestLoader.discover(listaa,
		pattern = 'start_*.py',
		top_level_dir = None)

	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)

	return testunit



alltestruns = creatsuitel()
#所有测试用例集

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#取当前时间
#filename = 'D:\\selenium_python\\report\\'+now+'result.html'
filename = "../Report\\" + now + "result.html"
fp = open(filename, 'wb')
#定义报告存放路径
runner = HTMLTestReportCN.HTMLTestRunner(
	stream = fp,
	title = u"自动化测试报告",
	description = u"自动化测试用例执行情况",
	tester = 'TANUKI')



def send_email(file_new):
	#发送邮箱服务器
	smtpserver = 'smtp.sohu.com'
	#发送邮箱用户名/密码
	user = 'fengyongming0311'
	password = '1qaz2wsx'
	#发送邮箱
	sender = 'fengyongming0311@sohu.com'
	#多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
	receiver = ['fengyongming@pujitech.com','fengyongming0311@sohu.com']
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
	os.chdir("../")
	#print (os.getcwd())
	result_dir = "Report\\"
	#result_dir = "..Report/"
	#print ("实际工作目录",os.getcwd())
	lists = os.listdir(result_dir)

	lists.sort(key = lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
	#上句为了找出最新的文件

	#print (u"最新测试生成的报告为：" + lists[-1])
	#找到最新生成的文件
	file_new = os.path.join(result_dir, lists[-1])

	#print ("发送的HTML文件名称为：============>", file_new)


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