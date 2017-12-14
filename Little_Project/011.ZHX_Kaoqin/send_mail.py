#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText


def send_mail(to_list,content):
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.163.com"
    mail_user="fengyongming0311@163.com"
    mail_pass="mican20130311"
    mail_postfix="163.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = "您好这是您这个月的考勤数据，请查看..."
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        print ("1")
        return True
    except Exception as e:
        print ("2")
        print (str(e))
        return False
