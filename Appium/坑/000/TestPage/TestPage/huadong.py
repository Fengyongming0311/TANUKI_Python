#coding:utf-8
__author__ = 'TANUKI'
from appium import webdriver
import time


#滑动是数值越小滑动的速度越快滑动的页面越多
#获得机器屏幕大小x,y
def getSize(driver):
	x = driver.get_window_size()['width']

	y = driver.get_window_size()['height']

	return (x, y)


#屏幕向上滑动
def shanghua(driver, t):
	l = getSize(driver)

	x1 = int(l[0] * 0.5)  #x坐标

	y1 = int(l[1] * 0.75)   #起始y坐标

	y2 = int(l[1] * 0.25)   #终点y坐标

	driver.swipe(x1, y1, x1, y2,t)


#屏幕向下滑动
def xiahua(driver, t):
	l = getSize(driver)

	x1 = int(l[0] * 0.5)  #x坐标

	y1 = int(l[1] * 0.25)   #起始y坐标

	y2 = int(l[1] * 0.75)   #终点y坐标

	driver.swipe(x1, y1, x1, y2,t)


#屏幕向左滑动
def zuohua(driver, t):
	l = getSize(driver)

	x1 = int(l[0]*0.75)

	y1 = int(l[1]*0.5)

	x2 = int(l[0]*0.05)

	driver.swipe(x1,y1,x2,y1,t)

#屏幕向右滑动
def youhua(driver, t):
	l = getSize(driver)

	x1 = int(l[0]*0.05)

	y1 = int(l[1]*0.5)

	x2 = int(l[0]*0.75)

	driver.swipe(x1,y1,x2,y1,t)


'''
#调用向左滑动  5为持续时间
zuohua(driver,1000)

#调用向右滑动
youhua(driver,1000)

#调用向上滑动
shanghua(driver,1000)

#调用向下滑动
xiahua(driver,1000)
'''