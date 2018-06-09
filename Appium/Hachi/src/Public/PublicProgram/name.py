#coding:utf-8
#一次性生成多个姓名
#xie = open('输出所有姓名.log')
import random
###############
'''
每次调用name生成随机姓名方法
import name
name.run(10000)

如果姓.txt 列表中用完的话用bak恢复重新使用
'''
###############
class CrateNamepy:
	def lastname(txtpath):
		try:
			ln = open('LastName.txt', 'r')
		except:
			ln = open(txtpath + '\\LastName.txt')
		du = ln.read()
		ln.close()
		name = list(set(du))
		#name 是左右的备选汉字
		all_list = [(one + two) for one in name for two in name]
		return all_list

	def firstname(txtpath):
		try:
			try:
				fn = open('FirstName.txt', 'r')
			except:
				fn = open(txtpath + '\\FirstName.txt', 'r')
			fname = fn.readlines()
			fn.close()
			#先用读的方式打开然后关闭，下次再以写的方式重新写入
			firstname = random.choice(fname)
			#随机取出一个姓
			firstname = firstname.strip()
			#去除后边的空格
			'''
			#若要取一个姓后从列表中删除这个姓，取消这些代码注释
			fname.remove(firstname)
			re = open('姓ANSI.txt', 'w+')
			re.writelines(fname)
			re.close()
			#若要取一个姓后从列表中删除这个姓，取消这些代码注释
			'''

			return firstname

		except Exception as e:
			print (e)
			pass

	def run(_cishu, txtpath = None):
		namelist = []
		xing = CrateNamepy.firstname(txtpath)
		ming = random.sample(CrateNamepy.lastname(txtpath), _cishu)

		for loop in range(_cishu):
			fullname = xing + ming[loop]
			namelist.append(fullname)

		namelist = set(namelist)
		namelist = list(namelist)
		return namelist













'''
玄妙的将两个列表的值遍历出来组成新的列表
list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C','注视我']


list3 = [(str(x) + y) for x in list1 for y in list2]
print (list3)
'''