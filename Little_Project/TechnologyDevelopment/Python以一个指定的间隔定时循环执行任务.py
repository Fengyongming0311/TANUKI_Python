__author__ = 'TANUKI'
#coding:utf-8

from datetime import date, time, datetime, timedelta

def work():
    '''
    这是要执行的程序
    '''
    print ("hello world.")


def runTask(func, day=0, hour=0, min=0, second=0):
    '''
    指定时间间隔循环执行任务
    :param func: 要执行的方法
    :param day:  传入天数
    :param hour: 传入小时数
    :param min:  传入分钟数
    :param second:  传入秒数
    :return: 没有返回值
    '''
    # Init time
    now = datetime.now()
    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
    # 获取当前时间
    print ("now:",strnow)
    #进入第一次循环
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period
    strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print ("next run:",strnext_time)
    while True:
        # Get system current time
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(strnext_time):
            # Get every start work time
            print ("start work: %s" % iter_now_time)
            # Call task func
            func()
            print ("task done.")
            # Get next iteration time
            iter_time = iter_now + period
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print ("next_iter: %s" % strnext_time)
            # Continue next iteration
            continue

runTask(work, second = 30)
#runTask(work, day=1, hour=2, min=1)