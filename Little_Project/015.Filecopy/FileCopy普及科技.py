#shutil 模块实现文件的复制
import os
import shutil

if os.path.exists("E:\\FYM_Python"):
	shutil.rmtree("E:\\FYM_Python")
	
else:
	print ("没找到文件夹,不用进行删除")

	

shutil.copytree('D:\FYM_Python', 'E:\FYM_python')
#后边的地址必须为不存在的文件夹

print ("文件拷贝完成...")



