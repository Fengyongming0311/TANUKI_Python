#coding:utf-8
__author__ = 'TANUKI'

import xlrd
import configparser
import datetime,os,sys,time
from xlrd import xldate_as_tuple
##################################################
#从Excel中读取数据
#显示周几
#超过早上10点打卡算迟到
#下班时间减去上班时间不足9小时，算早退
#最后以Excel显示
##################################################


def main():
	config = get_config()	#读取配置文件Config.ini

	#cfg_name = config.get('STAFF', 'name')	 #员工姓名

	#STAFF_name = cfg_name.split(',')

	filename = config.get("filename", "filename")

	data = xlrd.open_workbook(filename) #打开文件

	listname = config.get("list", "list")

	biao1 = data.sheet_by_name(listname)  #通过表名找到这个表！

	nrows = biao1.nrows	#获取共有多少行

	#创建所有数据的列表
	alldata = []
	
	#取所有日期信息
	date = []

	#取所有员工姓名
	allstaff = []

	

	for i in range(nrows):
		if (i == 0):
			continue	#当i == 0 第一行标题，直接略过
		######
		#这里处理328476.12736时间格式
		zhongzhuan = biao1.row_values(i)
		if isinstance(zhongzhuan[3], float):
			#xldate_as_tuple从excel中读取浮点数
			temp = datetime.datetime(*xldate_as_tuple(zhongzhuan[3], 0))
			zhongzhuan[3] = temp.strftime('%Y/%m/%d %H:%M:%S')
		else:
			#转换成时间数组
			zhongzhuan[3] = time.strptime(zhongzhuan[3], '%Y/%m/%d %H:%M:%S')
			#转换成新的时间格式('%Y/%m/%d %H:%M:%S')
			zhongzhuan[3] = time.strftime('%Y/%m/%d %H:%M:%S',zhongzhuan[3])
		######

		zhongzhuan = geshihuashuju(zhongzhuan)
		#zhongzhuan 是包含所有数据的列表单条的
		zhongzhuan[2] = chuli_time(zhongzhuan[2])       #对时间进行了处理
		#如果列表中的数据名字没在STAFF_name列表中，说明不是现役员工，PASS掉数据
		date.append(zhongzhuan[1])
		#这里把所有时间列出来
		allstaff.append(zhongzhuan[0])
		zhongzhuan = apm(zhongzhuan)
		
		alldata.append(zhongzhuan)

	date = datesort(date)

	allstaff = list(set(allstaff))
	#print (allstaff)


	#加入写Excel
	import xlwt
	workbook = xlwt.Workbook() #注意Workbook的开头W要大写
	sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok = True)
	#cell_overwrite_ok参数用于确认同一个cell单元是否可以重设值。
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = 'SimSun'    # 指定“宋体”
	font.height = 230
	style.font = font
	#上设置字体
	borders = xlwt.Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	borders.bottom_colour = 0x3A
	style.borders = borders
	#上设置框线

	alignment = xlwt.Alignment()
	alignment.horz = xlwt.Alignment.HORZ_CENTER    #水平居中
	alignment.vert = xlwt.Alignment.VERT_CENTER    #垂直居中
	style.alignment = alignment
	#设置字体居中
	first_col = sheet1.col(0)
	first_col.width = 270 * 20

	second_col = sheet1.col(1)
	second_col.width = 270 * 20

	third_col = sheet1.col(2)
	third_col.width = 270 * 20

	fourth_col = sheet1.col(3)
	fourth_col.width = 270 * 20

	fifth_col = sheet1.col(4)
	fifth_col.width = 270 * 20

	sixth_col = sheet1.col(5)
	sixth_col.width = 270 * 20

	seventh_col = sheet1.col(6)
	seventh_col.width = 270 * 20

	#上设置横行的长度

	################设置第一行字体的格式###############
	geshi = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = 'SimSun'    # 指定“宋体”
	font.height = 350
	font.bold = 'on'
	geshi.font = font
	#上设置字体
	borders = xlwt.Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	borders.bottom_colour = 0x3A
	geshi.borders = borders
	##############设置第一行字体的格式完成#############


	sheet1.write(0, 0, '姓名', geshi)
	sheet1.write(0, 1, '日期', geshi)
	sheet1.write(0, 2, '上班打卡', geshi)
	sheet1.write(0, 3, '下班打卡', geshi)
	sheet1.write(0, 4, '漏打卡', geshi)
	sheet1.write(0, 5, '迟到', geshi)
	sheet1.write(0, 6, '是否早退', geshi)

	num = 1

	#现在只要把单个人的数据穿进去就能得出单个人的整合数据了	
	for name in allstaff:
		app = []
		for i in alldata:
			if name == i[0]:
				app.append(i)


		last_data = data_merge(app, date)                                 #合并上下班日期，上班取最早下班取最晚
		for don in last_data:
			
			#最终数据在这里！！！！
			don = get_week_day(don)											#判断日期是周几
			don = loudaka(don)												#判断漏打卡
			don = daylate(don)                                              #判断上班是否迟到
			don = worktime(don)                                             #判断是否早退
			#print (don[0],'%',don[1],'%',don[2],'%',don[3],'%',don[4],'%',don[5],'%',don[6])

			sheet1.write(num, 0, don[0] , style)#姓名
			sheet1.write(num, 1, don[1] , style)#日期
			sheet1.write(num, 2, don[2] , style)#上班打卡
			sheet1.write(num, 3, don[3] , style)#下班打卡
			sheet1.write(num, 4, don[4] , style)#漏打卡
			sheet1.write(num, 5, don[5] , style)#迟到
			sheet1.write(num, 6, don[6] , style)#是否早退
			print (num)

			
			num = num + 1


	#跳出循环后保存Excel
	now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
	workbook.save(now + '生成统计结果.xls')
	print ("===================统计完成===================")

	'''
	#这是按照配置文件姓名排序的
	for name in STAFF_name:
		app = []
		for i in alldata:
			if name == i[0]:
				app.append(i)
		

		last_data = data_merge(app, date)
		for don in last_data:
			#print (don)
			pass
	'''


#判断是否早退，上班打卡和上班打卡时差大于就小时算正常
def worktime(data):
	if not data[2] == '' and not data[3] == '':
		time1 = datetime.datetime.strptime(data[2], '%H:%M:%S')
		time2 = datetime.datetime.strptime(data[3], '%H:%M:%S')

		times = str((time2 - time1)).split(":")
		if int(times[0]) >= 9:
			data.append("")
		else:
			data.append("打卡时间不足9小时")
	else:
		data.append("")

	return data

#判断上班是否迟到，上班打卡超过10点判定为迟到
def daylate(data):
	if not data[2] == '':
		time1 = datetime.datetime.strptime(data[2], '%H:%M:%S')
		time2 = datetime.datetime.strptime("10:00:59", '%H:%M:%S')
		#哈哈哈哈哈这里修改一下10:00:59内都不算迟到
		if time1 > time2:
			data.append("上班迟到" + data[2])
		else:
			data.append("")

	else:
		data.append("")
	return data


#判断漏打卡
def loudaka(data):
	#上班与下班都有打卡时间 加入空
	if not data[2] == '' and not data[3] == '':
		data.append("")
	#漏打上班卡
	elif data[2] == '' and not data[3] == '':
		data.append("未打上班卡")
	elif not data[2] == '' and data[3] == '':
		data.append("未打下班卡")
	elif data[2] == '' and data[3] == '':
		xingqi = data[1][-2:]
		if xingqi == '周六' or xingqi == '周日':
			#data.append(xingqi)
			data.append("")
		else:
			data.append("旷工一天")


	return data

		


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
	del zhongzhuan[1]   #再次删除考勤号码列
	for m in range(5):
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


import time,datetime
#判断当前日期是周几
def get_week_day(date):
	week_day_dict = {
		0 : '周一',
		1 : '周二',
		2 : '周三',
		3 : '周四',
		4 : '周五',
		5 : '周六',
		6 : '周日',
  }
	
	day = datetime.datetime.strptime(date[1], '%Y/%m/%d').weekday()
	date[1] = date[1] + " " + week_day_dict[day]
	return date

if __name__ == "__main__":
	main()