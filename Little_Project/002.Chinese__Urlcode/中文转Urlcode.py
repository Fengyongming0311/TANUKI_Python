import urllib
from urllib import parse
"""
直接写from urllib import parse 找不到
得在前边引用urllib才能用

每次写完覆盖源文件
"""
file_name = open("Chinese_name.txt" , "r")

str = file_name.readlines()

file_name.close()
#用完关闭
#str = str.encode('gb2312')
def chuli_data(_str):
	f = open("转码后输出.log", "w")

	for i in _str:
		i = i.strip()
		m = {'zhuanhua': i}
		s = urllib.parse.urlencode(m)
		final = s.strip("zhuanhua=") + '\n'
		'''
		如果是编译输出直接复制的话就这么写
		final = s.strip("zhuanhua=")
		'''
		f.writelines(final)
	f.close()



chuli_data(str)
