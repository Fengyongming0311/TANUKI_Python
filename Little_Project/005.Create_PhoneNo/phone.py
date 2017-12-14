import random
def phone():
	phone1 = '13'
	phone2 = random.randint(0,999999999)
	if phone2 < 10:
		phone2 = '00000000' + str(phone2)
	elif 10 <= phone2 < 100:
		phone2 = '0000000' + str(phone2)
	elif 100 <= phone2 < 1000:
		phone2 = '000000' + str(phone2)
	elif 1000 <= phone2 < 10000:
		phone2 = '00000' + str(phone2)
	elif 10000 <= phone2 < 100000:
		phone2 = '0000' + str(phone2)
	elif 100000 <= phone2 < 1000000:
		phone2 = '000' + str(phone2)
	elif 1000000 <= phone2 < 10000000:
		phone2 = '00' + str(phone2)
	elif 10000000 <= phone2 < 100000000:
		phone2 = '0' + str(phone2)
	else:
		phone2 = str(phone2)

	phone = phone1 + phone2
	return phone



def run(_cishu):
	phone_list  = []
	for i in range(_cishu):
		phoneNO = phone()
		phone_list.append(phoneNO)

	phone_list = set(phone_list)
	
	for don in phone_list:
		print (don)
	print ("成功生成%d个手机号。"%len(phone_list))

