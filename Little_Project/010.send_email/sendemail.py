__author__ = "TANUKI"
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import time


def send_email():

    #发送邮箱服务器
    smtpserver = 'smtp.sohu.com'
    #发送邮箱用户名/密码
    user = 'fengyongming0311'
    password = '1qaz2wsx'
    #发送邮箱
    sender = 'fengyongming0311@sohu.com'
    #多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['342469367@qq.com','fengyongming@pujitech.com']
    #发送邮件主题
    subject = '我是雷神托尔，为了北方神的荣耀！！'
    mailfrom = '自动化测试结果邮件 <fengyongming0311@sohu.com>'
    #这里填写邮件发送自XXXXXXXXXXXXXXXX

    msg = MIMEMultipart('mixed')
    #混合型邮件类型，包括纯文本和html，图片声音等

    '''
    这里是发送邮件的内容
    '''
    #构造文字内容
    text = """  你好小邢，明天的考试请你加油，如果明天我陪你去考试的话请告诉我具体的地址在哪里我好想听说是在石景山区，咱们得开车去了，早上七点走你看好不好？
    """
    text_plain = MIMEText(text,'plain', 'utf-8')
    msg.attach(text_plain)


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


def getTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))



send_email()