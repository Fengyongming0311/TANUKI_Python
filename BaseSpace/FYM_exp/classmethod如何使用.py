class Data_test(object):
	day=0
	month=0
	year=0
	def __init__(self,year=0,month=0,day=0):
		self.day=day
		self.month=month
		self.year=year

	def out_date(self):
		print ("year :")
		print (self.year)
		print ("month :")
		print (self.month)
		print ("day :")
		print (self.day)

#t=Data_test(2016,8,1)
#t.out_date()
"""
string_date='2016-8-1'
year,month,day=map(int,string_date.split('-'))
s = Data_test(year,month,day)
s.out_date()
"""

class Data_test2(object):
	day=0
	month=0
	year=0

	def __init__(self,year=0,month=0,day=0):
		self.day=day
		self.month=month
		self.year=year
	#
	#在Date_test类里面创建一个成员函数，前面用了@classmethod装饰。 它的作用就是有点像静态类，比静态类不一样的就是它可以传进来一个当前类作为第一个参数。
	#这样子等于先调用get_date()对字符串进行出来，然后才使用Data_test的构造函数初始化。
	#这样的好处就是你以后重构类的时候不必要修改构造函数，只需要额外添加你要处理的函数，然后使用装饰符 @classmethod 就可以了。
	#self是指类的实例，二cls值得是类定义
	#
	@classmethod
	def get_date(cls,string_date):
		#这里第一个参数是cls， 表示调用当前的类名
		year,month,day = map(int,string_date.split('-'))
		date1 = cls(year,month,day)
		#返回的是一个初始化后的类
		#print ("这是date1的值",date1.year,date1.month,date1.day)
		return date1

	def out_date(self):
		print ("year :")
		print (self.year)
		print ("month :")
		print (self.month)
		print ("day :")
		print (self.day)




#r = Data_test2.get_date("2016-10-18")
r = Data_test2(2016,8,1)
r.out_date()

print ("##########################################################")

don = Data_test2.get_date("2016-10-18")
#don = Data_test2.get_date(2016,8,1)
don.out_date()