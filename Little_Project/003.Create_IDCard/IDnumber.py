#coding:utf-8
#2016.9.7 17:15
#V1.00  实现基本功能
#V1.01  将生日变为随机数，岁数大于18岁
'''
110102      19890311      15      5      4
身份证分为开头六位数字，加出生年月日8位，加两位随机位，加男性为单数随机数女性为双数随机数，加校验位总共18位身份证号
head       定义为开头
breath     出生年月日
randomNO   为两位随机数
sex        为性别校验随机数
count      为head+breath+randomNO+sex  计算权重的数字
check      为最后一位校验位
IDnumber   为最后生成的身份证号
'''
import random

##########head区##########
def head():
	f = open('最新区县号码.txt', 'r')
	readNO = f.readlines()

	_head = str((random.choice(readNO)).strip())
	
	#从区县列表中取随机数

	#print (head)
	#print (type(head))
	return _head
##########################


#######随机breath区#######
'''
beath区又分为
year  年
month 月
day   日
'''
def beath():
	ye = [198,199]
	year = str(random.choice(ye)) + str(random.randint(0,9))
	#暂定岁数为20 以上
	if int(year) > 1996:
		year = str(int(year) - 3)
	#print (year)

	month = random.randint(1,12)
	if month < 10:
		month = '0' + str(month)
	else:
		month = str(month)
	#print (month)

	#哈哈哈哈这句话好可笑if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
	if int(month) in [1,3,5,7,8,10,12]:
		day = random.randint(1, 31)
		if day < 10:
			day = '0' + str(day)
	elif int(month) in [4,6,9,11]:
		day = random.randint(1, 30)
		if day < 10:
			day = '0' + str(day)
	else:
		day = random.randint(1, 28)
		if day < 10:
			day = '0' + str(day)

	_beath = year + month + str(day)
	return _beath

##########################
'''
####指定年月日breath区####
def beath():
	_beath = '19890311'
	#手动写死
	return _beath
##########################
'''

########randomNO区########
def randomNO():
	
	_randomNO = random.randint(0,99)
	if _randomNO < 10:
		_randomNO = '0' + str(_randomNO)
	else:
		_randomNO = str(_randomNO)
	#print (_randomNO)
	#print (type(_randomNO))
	
	return _randomNO

##########################



##########sex区###########
#male 男性   female 女性
def sex():
	malelist = [1, 3, 5, 7, 9]
	femalelist = [0, 2, 4, 6, 8]
	#下这里手动输入:    1 为男性  2为女性
	xingbie = 1
	if xingbie == 1:
		_sex = random.choice(malelist)
	else:
		_sex = random.choice(femalelist)

	_sex = str(_sex)
	#print (sex)
	return _sex
##########################

#########check区##########
def check(__count):
	Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
	# Wi 是一个由国家用于加权计算的值，是一个固定的值，就是用身份证号第一位*7 第二位*9 第三位*10 ...一共是17位
	#IndexTable 是最后算出加权数字之后推算出的数字
	IndexTable = {
		0 : '1',
		1 : '0',
		2 : 'X',
		3 : '9',
		4 : '8',
		5 : '7',
		6 : '6',
		7 : '5',
		8 : '4',
		9 : '3',
		10 : '2'}
	def calculate(identity):
		sum = 0
		No = list(identity)
		for i in range(17):
			sum = sum + (int(No[i]) * Wi[i])

		Index = sum % 11
		return IndexTable[Index]


	_check = calculate(__count)
	return _check

##########################

def IDnumber(_count):
	_check = check(_count)
	_IDnumber = _count + _check
	return _IDnumber




def run(_loop):
	for i in range (_loop):
		count = head() + beath() + randomNO() + sex()
		cardID = IDnumber(count)
		print (cardID)
