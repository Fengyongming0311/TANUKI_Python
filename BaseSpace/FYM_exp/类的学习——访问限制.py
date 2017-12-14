class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print ('%s: %s' % (self.__name, self.__score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
	#但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	#如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：
	#def set_score(self, score):
		#self.__score = score

	#set_score防止传入无效参数
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

bart = Student('Bart Simpson', 59)
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了
#print (bart.__name)
#这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
#健壮后测试get_name()
#print (bart.get_name())
#print (bart.get_score())
#测试set_score
try:
	#bart.set_score(0)
	bart.set_score(89)
	#bart.set_score(199)
	#bart.set_score("dondake")
	
except Exception as e:
	print (e)
print (bart.get_score())
























"""bart = Student('Bart Simpson', 99)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
"""