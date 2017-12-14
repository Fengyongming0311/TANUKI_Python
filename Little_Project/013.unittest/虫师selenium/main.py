#coding:utf-8
__author__ = "TANUKI"

import testrun_part1
import sendmail_part2
import time
if __name__ == '__main__':
	testrun_part1.runner.run(testrun_part1.creatsuitel())
	#执行测试用例
	time.sleep(3)
	testrun_part1.fp.close()
	#跑完脚本等待３秒把报告文件关闭然后发送邮件
	sendmail_part2.sendreport()
	#执行发邮件