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
	
	day = datetime.datetime.strptime(date, '%Y/%m/%d').weekday()

	return week_day_dict[day]


date = '2017/7/13'

print (get_week_day(date))