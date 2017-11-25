#coding:utf-8
import os,datetime,time
import sys
sys.path.append("\\report")
result_dir = "report\\"

lists = os.listdir(result_dir)
#print (lists)

lists.sort(key = lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
#上句为了找出最新的文件
print ("最新的文件为：" + lists[-1])

file = os.path.join(result_dir, lists[-1])


print (file)