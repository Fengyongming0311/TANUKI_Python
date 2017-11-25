表示之后的为注释  #
'''
注释多行
'''


同一行书写多个语句
import sys; x = 'foo'; sys.stdout.write(x + '\n')



变量赋值
a = 13
b = 'python的变量赋值'



python数据类型
1、字符串
2、布尔类型
3、整数
4、浮点数
5、数字
6、列表
7、元组
8、字典
9、日期


1.字符串：
dondake='我是dondake'
print (dondake)


2.布尔类型：
dondake = False    （dondake = 0）
dondake = True      （dondake = 1）


3.整数：
bnt=20
print  (bnt)

4.浮点数：
eloat = 2.4 
print (eloat)

5.数字：
包括整数和浮点数（包括数字类型转换和数学函数）
abs(x)    返回数字的绝对值，如abs(-10) 返回 10
max(x1, x2,...)    返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)    返回给定参数的最小值，参数可以为序列。


6.列表：

list=['physics', 'chemistry', 1997, 2000]
nums=[1, 3, 5, 7, 8, 13, 20]


访问列表的值：

nums[0]                #为1
num[2:5]               #为    [5, 7, 8] 从下标为2的元素切割到下标为5的元素，但不包含下标为5的元素
nums[1:]               # [3, 5, 7, 8, 13, 20] 从下标为1切割到最后一个元素
nums[:-3]             #为 [1, 3, 5, 7] 从最开始的元素一直切割到倒数第3个元素，但不包含倒数第三个元素'''
nums[:]                 #   [1, 3, 5, 7, 8, 13, 20] 返回所有元素


更新列表：
nums = [0,3,5,7,8,9,15]
nums[0] = "fym"
print (nums)
输出为：['fym', 3, 5, 7, 8, 9, 15]


删除列表元素
del nums[0];
print "nums[:]:", nums[:];
输出为：nums[:]:   [3, 5, 7, 8, 13, 20]

列表脚本操作
print len([1, 2, 3]); #3
print [1, 2, 3] + [4, 5, 6]; #[1, 2, 3, 4, 5, 6]
print ['Hi!'] * 4; #['Hi!', 'Hi!', 'Hi!', 'Hi!']
print 3 in [1, 2, 3] #True
for x in [1, 2, 3]: print x, #1 2 3


列表截取
L=['spam', 'Spam', 'SPAM!'];
print L[2]; #'SPAM!'
print L[-2]; #'Spam'
print L[1:]; #['Spam', 'SPAM!']

列表排序函数
list = [1,5,8,2,77,3,2,86,123,41,22]
don = sorted(list)  
做了一个复制并排序

print (don) 

7.元组(tuple)
Python的元组与列表类似，不同之处在于元组的元素不能修改；元组使用小括号()，列表使用方括号[]；元组创建很简单，只需要在括号中添加元素，并使用逗号(,)隔开即可。

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

元组中只有一个元素时，需要在元素后面添加逗号，例如：tup1 = (50,)
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，例如:
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup 2
print (tup3)
输出：(12, 34.56, 'abc', 'xyz')



删除元组
元组中的元素值是不允许删除的，可以使用del语句来删除整个元组，例如:
tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;


元组索引&截取
L = ('one', 'two', 'three!');
print (L[2])  #three!
print (L[-2]) #two   因为three是-3
print (L[1:]) #('two', 'three!')


元组内置函数
len(tuple) 计算元组元素个数。
max(tuple) 返回元组中元素最大值。
min(tuple) 返回元组中元素最小值。


tup1 = (1,2,3)
tup2 = (5,6,7)
print(len(tup1))   输出3
print (max(tup2))  输出7
print (min(tup1))  输出1



8、字典
字典(dictionary)是除列表之外python中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典由键和对应的值组成。字典也被称作关联数组或哈希表。基本语法如下：

zidian = {'xingming': 'fengyongming', 'shengri': int(1989), 'phoneNO': 13466738904}
print (zidian )
输出：{'xingming': 'fengyongming', 'shengri': 1989, 'phoneNO': 13466738904}


字典中一个KEY对应多个值：
zidian = {'xingming': ['fengyongming',13466738904],'shengri': int(1989), 'phoneNO': 13466738904}
print (zidian['xingming'])


访问字典里的值

dict = {'name': 'Zara', 'age': 7, 'class': 'First'};
print (dict['name'])   
print (dict['age'])
输出：Zara
	7

修改字典
dict = {'name': 'Zara', 'age': 7, 'class': 'First'};
dict["age"] = 27   #修改已有键的值
dict["school"] ="wutong"   #增加新的键/值对
print (dict['age'])
print (dict['school'])
####################################################
输出    27
	wutong



删除字典
del dict['name']     # 删除键是'name'的条目
dict.clear()            # 清空词典所有条目
del dict                  # 删除词典
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}
del dict['name']
print (dict)

#########################################################
条件循环语句
if else


score = 66
if score<60:
    print ("不及格")
else:
	print ("及格")

if elif else

score = 60
if score<60:
    print ("D")
elif score<80:
    print ("C")
elif score<90:
    print ("B")
else:
    print ("A")




for循环

world=['China','England','America']
for i in world:
    print (i)

range内建函数  ==   

num = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(num)):
	print (i)


for语句也可以else语句块中止，可可以和break和continue一块使用
 for target in object:
     # statementSuite1
     if boolenExpression1:
         break
     if boolenExpression2:
         continue
 else:
     statementSuite2
for循环正常退出后，执行else块
break语句提供了for循环的异常退出，跳过else子句
continue语句终止目前的循环异常，继续循环余下的部分


while循环

count = 0 
while (count < 9):
	print ('The index is:', count)
	count += 1

无限循环
while True:
	print ("无限循环")

while+ else

count=5
while count>0:
    print ('i love python')
    count=count-1
else:
    print ('over')



break语句
count = 0 
while (count < 9):
	print ('The index is:', count)
	count += 1
	if count == 4:
		break

pass 语句
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)
print ("Good bye!")


异常处理
def into_jinjianshenqing():	
	try:
		time.sleep(1)
		driver.switch_to_frame('mainFrame')
		time.sleep(1)
		driver.switch_to_frame('leftFrame')
		WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("/html/body/div/ul[2]/li[1]/a")) #wait
		driver.find_element_by_xpath("/html/body/div/ul[2]/li[1]/a").click()
		driver.switch_to_default_content()    #退出框架

	except Exception as e:
		print ("转入进件申请BUG==============:",e)

	finally:
		pass


函数 
def plus(_num1,_num2):
	return (_num1+_num2)


a = 1
b = 2
c = plus(a,b)


print (c)



匿名函数  lambda
匿名 就是 不需要以标准的方式来声明，
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector("select[id=\"loan_time\"][class=\"select_styleN1\"]"))

driver.find_element_by_css_selector("select[id=\"loan_time\"][class=\"select_styleN1\"]").find_element_by_xpath("/html/body/div[2]/div/form/ul[2]/li[4]/div/div[1]/select/option[3]").click()




引用各种模块
import var     引用

var.tim(a,b)

from module import var
tim(a,b)

from module import *   (不是良好的变成风格)
区别



面向对象编程



什么是json：

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。易于人阅读和编写。同时也易于机器解析和生成。它基于JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999的一个子集。JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C, C++, C#, Java, JavaScript, Perl, Python等）。这些特性使JSON成为理想的数据交换语言。

JSON建构于两种结构：

“名称/值”对的集合（A collection of name/value pairs）。不同的语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。
值的有序列表（An ordered list of values）。在大部分语言中，它被理解为数组（array）。
这些都是常见的数据结构。事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
