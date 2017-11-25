#shutil 模块实现文件的复制

import shutil
'''
Rmtree源码
shutil.rmtree("E:\\test\\b")
可以发现b文件夹连同下面的文件都消失了。



Move源码
同上，看名字就知道的功能，类似于windows的ctrl+x->ctrl+v操作。
shutil.move("E:\\test\\a", "E:\\test\\b")
'''


shutil.copytree('D:\\越狱第一季', 'C:\\越狱第一季')
#后边的地址必须为不存在的文件夹



