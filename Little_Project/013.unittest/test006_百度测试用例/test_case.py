#-*-coding=utf-8 -*-
import os
#列出某个文件夹下的所有 case,这里用的是 python，
#所在 py 文件运行一次后会生成一个 pyc 的副本
caselist=os.listdir('E:\\FYM_Python\\Little_Project\\013.unittest\\test006_百度测试用例\\test_case')
for a in caselist:
	s = a.split('.')[1] #选取后缀名为 py 的文件
	
	if s == 'py':
	#此处执行 dos 命令并将结果保存到 log.txt
		os.system('E:\\FYM_Python\\Little_Project\\013.unittest\\test006_百度测试用例\\test_case\\%s 1>>log.txt 2>&1'%a)
	else:
		print ("这个文件不是Python可执行文件....%s" %a)