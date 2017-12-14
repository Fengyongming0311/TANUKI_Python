#shutil 模块实现文件的复制
import os
import shutil

if os.path.exists("E:\\TANUKI_Python"):
	shutil.rmtree("E:\\TANUKI_Python")
	
else:
	print ("没找到文件夹,不用进行删除")

	

shutil.copytree('D:\TANUKI_Python', 'E:\TANUKI_Python')
#后边的地址必须为不存在的文件夹

print ("文件拷贝完成...")



