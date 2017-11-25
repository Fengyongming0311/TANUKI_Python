#coding:utf-8
__author__ = 'TANUKI'

import xlrd
import configparser
import datetime,os,sys,time
##################################################
#从Excel中读取数据
##################################################


def main():
	config = get_config()	#读取配置文件Config.ini

	cfg_name = config.get('STAFF', 'name')	 #员工姓名

	STAFF_name = cfg_name.split(',')

	filename = config.get("filename", "filename")

	data = xlrd.open_workbook(filename) #打开文件

	listname = config.get("list", "list")

	biao1 = data.sheet_by_name(listname)  #通过表名找到这个表！

	nrows = biao1.nrows	#获取共有多少行

	alldata = []
	#创建所有数据的列表
	date = []

	for i in range(nrows):
		if (i == 0):
			continue	#当i == 0 第一行标题，直接略过
		zhongzhuan = geshihuashuju(biao1.row_values(i))
		#zhongzhuan 是包含所有数据的列表单条的
		zhongzhuan[2] = chuli_time(zhongzhuan[2])       #对时间进行了处理
		#如果列表中的数据名字没在STAFF_name列表中，说明不是现役员工，PASS掉数据
		date.append(zhongzhuan[1])
		#这里把所有时间列出来
		zhongzhuan = apm(zhongzhuan)
		
		alldata.append(zhongzhuan)

	date = datesort(date)
	
	for name in STAFF_name:
		app = []
		for i in alldata:
			if name == i[0]:
				app.append(i)
		

		last_data = data_merge(app, date)
		for don in last_data:
			print (don)

	#现在只要把单个人的数据穿进去就能得出单个人的整合数据了	




#通过相同的姓名和日期合并数据
def data_merge(app, date):
	#print (app)
	#print (date)
	allshuju = []
	
	for evday in date:
		#print (evday)
		
		merge = ['', '', '', '']
		merge[1] = evday
		for evdata in app:
			merge[0] = evdata[0]

			if evdata[1] == evday:
				#print (evdata)
				#判断上班打卡时间        取最早的打卡时间
				#case1: 数据空  case为空    pass
				if merge[2] == '' and evdata[2] == '':
					pass
				#case2: 数据空  case不为空   取case
				elif merge[2] == '' and not evdata[2] == '':
					merge[2] = evdata[2]
				#case3: 数据不为空  case为空   pass
				elif not merge[2] == '' and evdata[2] == '':
					pass
				#case4: 数据不为空  case不为空    比较大小，取最小值
				elif not merge[2] == '' and not evdata[2] == '':
					time1 = datetime.datetime.strptime(merge[2], '%H:%M:%S')
					time2 = datetime.datetime.strptime(evdata[2], '%H:%M:%S')
					if time1 < time2:
						pass
					elif time1 > time2:
						merge[2] = evdata[2]
					else:
						pass

				
				#判断下班打卡时间        取最晚的打卡时间
				#case1: 数据空  case为空    pass
				if merge[3] == '' and evdata[3] == '':
					pass
				#case2: 数据空  case不为空   取case
				elif merge[3] == '' and not evdata[3] == '':
					merge[3] = evdata[3]
				#case3: 数据不为空  case为空   pass
				elif not merge[3] == '' and evdata[3] == '':
					pass
				#case4: 数据不为空  case不为空    比较大小，取最大值
				elif not merge[3] == '' and not evdata[3] == '':
					time1 = datetime.datetime.strptime(merge[3], '%H:%M:%S')
					time2 = datetime.datetime.strptime(evdata[3], '%H:%M:%S')
					if time1 < time2:
						merge[3] = evdata[3]
					elif time1 > time2:
						pass
					else:
						pass
		#最后
		if not merge[0] == '':
			allshuju.append(merge)
	return allshuju
		



	#最后
	#print ('所有数据',allshuju)





#判断是上班时间还是下班时间(普及的打卡不涉及空数据的问题)
def apm(time):
	#print (time)
	try:
		rentime = datetime.datetime.strptime(time[2], '%H:%M:%S')
		zhengwutime = datetime.datetime.strptime('12:00:00', '%H:%M:%S')
		if rentime < zhengwutime:
			#print (rentime,"上午")
			time.append("")
			return time
		elif rentime > zhengwutime:
			#print (rentime,"下午")
			don = time[2]
			time[2] = ''
			time.append(don)
			return time
		elif rentime == zhengwutime:
			#print (rentime,"中午12点")
			time.append("")
			return time
	except Exception as e:
		time.append("")
		return time


#处理上下班时间
def chuli_time(lie_time):
	#把 9:28:03 变成 09:28:03 因为try中只处理float的数据所以 直接的str时间也需要在except中增加处理
	#使用replace(' ' , '')去除中间空格
	try:
		float(lie_time)
		new_time = float(lie_time)
		new_time = xlrd.xldate_as_tuple(new_time ,0)
		d = new_time[3]
		if (d < 10):
			d = '0' + str(d)
		else:
			d = str(new_time[3])
		e = new_time[4]
		if (e < 10):
			e = '0' + str(e)
		else:
			e = str(new_time[4])
		f = new_time[5]
		if (f < 10):
			f = '0' + str(f)
		else:
			f = str(new_time[5])
		return (d + ":" + e + ":" + f)
	except:
		if (lie_time == ''):		#判断传入空字符串直接退出方法
			return lie_time
		lie_time = lie_time.replace(' ' ,'')
		(a,b,c) = lie_time.split(':')
		if (int(a) < 10):
			a = int(a)
			a = '0' + str(a)
		'''
		if (int(b) < 10):
			b = '0' + b
		if (int(c) < 10):
			c = '0' + c
		'''
		return (a + ":" + b + ":" + c)




#获取配置文件把节假日等不可控日期写在配置文件中
def get_config():
	config = configparser.ConfigParser()
	config_file = open('Config.ini')
	config.readfp(config_file)
	config_file.close()

	return config

#格式化初始数据，删除不必要的列
def geshihuashuju(zhongzhuan):
	del zhongzhuan[0]	#删除第一行部门数据
	for m in range(4):
		del zhongzhuan[2]	#删除机器号#删除编号#删除比对方式#删除卡号
	try:
		date, time = zhongzhuan[1].split(' ')	
	except Exception as e:
		date = ''
		time = ''

	#将zhongzhuan中的日期和时间分离为两个数据
	del zhongzhuan[1]	#删除时间和日期一条list数据
	zhongzhuan.append(date)
	zhongzhuan.append(time)
	return zhongzhuan

#对date进行从小到大的排序
def datesort(date):
	date = list(set(date))
	for i in range(0, len(date)):
		for j in range (0, i):
			if datetime.datetime.strptime(date[i], '%Y/%m/%d') <= datetime.datetime.strptime(date[j], '%Y/%m/%d'):
				date[i],date[j] = date[j],date[i]
		

	

	return date


if __name__ == "__main__":
	main()