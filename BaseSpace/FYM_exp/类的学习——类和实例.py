class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	#pipei001
	#def print_score(std):
		#print ('%s: %s' % (std.name, std.score))

	#但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法如下如下如下：
	def print_score(self):
		print ('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 59)
#print (bart.name)
#print (bart.score)

#这是用外部函数调用的pipei001
#Student.print_score(bart)
bart.print_score()
#这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。 这就是封装！！！！！封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
#print (bart.get_grade())

############################################################
#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
bart = Student('Bart Simpson', 99)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
#print (bart.age)
#下AttributeError: 'Student' object has no attribute 'age'
#print (lisa.age)
bart.print_score()