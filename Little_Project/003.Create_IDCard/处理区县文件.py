#coding:utf-8
#2016.9.7 16:37

#读取各地区数字用在身份证号生成中

don = open('最新县及县以上行政区划代码（截止2015年9月30日）.txt', 'r')
dondake = don.readlines()

new_don = list(set(dondake))
new_don.sort(key = dondake.index)
try:
	new_don.remove('\n')
except Exception as e:
	#print (e)
	pass

lastfile = open("最新区县号码.txt", 'w')


for i in new_don:
	i = i.strip()
	num = i[0:6] + '\n'
	lastfile.writelines(num)

lastfile.close()



'''
列表去重的几种方法
dondake = don.readlines()

1.最基础的方法
new_don = []

for i in dondake:
	if i not in new_don:
		new_don.append(i)

print (new_don)


2.第二种这样的话不会保持列表的原来顺序
dondake = list(set(dondake))
print (dondake)


3.按照索引再次排序
new_don = list(set(dondake))
new_don.sort(key = dondake.index)
print (new_don)


'''


'''
for i in range(len(dondake)):
	print (i)
'''