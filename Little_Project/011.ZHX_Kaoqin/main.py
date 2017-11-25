#coding:utf-8
# -*- coding: utf-8 -*-

#从Execl读取数据出来
#应该最先判断日期是平时上班 ，还是周末还是假期
#然后就能判断上班是否迟到
#然后判断是否为加班
#然后判断是否为同一个人的打卡时间，一个人有可能打多次卡，算最后一次的
#最后统计平时加班多少，节假日加班多少，是否有漏打卡，是否有未刷上班或者下班卡
#发送统计邮件给每个人(可以从配置文件中读取出来)
#如果早上上班漏打卡不计算迟到！！
#因为有两个指纹和一个工卡，需要整合打卡时间数据，通过匹配姓名+日期，如果相同就把数据整合到一起
#工作日无打卡记录，旷工或者请假
############优化#############
#整理数据
#清洗数据
#提取数据
#############################
#发邮件的时候把用户的详细打卡记录也附在下边这样可信度比较高
#ZHX节假日前一天提前放假的上半天班的！！！
#没有计算早退情况

import xlrd
import configparser
import datetime
import FYM_config
import send_mail

def main():
    config = get_config()  #读取配置文件Myfirst.ini

    STAFF_name = FYM_config.The_Name()

    data = xlrd.open_workbook('wanghuan.xls') #打开文件

    biao1 = data.sheet_by_name(u'Sheet1')  #通过表名找到这个表1！

    nrows = biao1.nrows    #获取共有多少行

    all_in = []

    for i in range(nrows):
        if (i == 0):
            continue   #当i == 0 第一行是上班时间下班时间等标题，直接略过

        zhongzhuan = biao1.row_values(i)   #抓取总表数据按照每行存储
        geshihuashuju(zhongzhuan)         #格式化显示数据
        print (zhongzhuan[4])
        print (type(zhongzhuan[4]))
        shangban_time = chuli_time(zhongzhuan[4])
        xiaban_time = chuli_time(zhongzhuan[5])

        zhongzhuan = zhongzhuan[0:4]

        zhongzhuan.append(shangban_time)

        zhongzhuan.append(xiaban_time)

        all_in.append(zhongzhuan)   #把单条zhongzhuan全部添加到all_in 中

    last_data = data_merge(all_in)       #执行整合



def fasongyoujian(dizhi,neirong):
    if send_mail.send_mail(dizhi,neirong):
        print ("发送成功")
    else:
        print ("发送失败")

#通过姓名的配置文件找到属于自己的数据然后整合到一起准备发邮件
#哈哈哈哈哈进来不用return 直接打印出来就是最终目标了！！
def tongjizhenghe(_honban , _STAFF_name):
    for name in _STAFF_name:
        #找出了商房自己人，排除金融街员工
        count_pingshi = 0  #统计平时加班时长
        count_zhoumo = 0   #统计周末加班时长
        count_chidao = 0   #统计迟到次数
        gerenhuizong = []
        for ever_list in _honban:
            #名字不在列表中的话continue
            if not name == ever_list[1]:
                continue
            #名字在列表中
            if name == ever_list[1]:
                count_pingshi = count_pingshi + float(ever_list[6])
                count_zhoumo = count_zhoumo + float(ever_list[7])
                if not ever_list[8] == '0':
                    count_chidao = count_chidao + 1
            xiangxi = str("姓名: %s 日期: %s 上班时间: %s 下班时间: %s 当日加班(平时): %.2f 当日加班(节假): %.2f 当日迟到时长: %s"
                       %(ever_list[1] ,ever_list[2] ,ever_list[3] ,ever_list[4] ,float(ever_list[6]) ,float(ever_list[7]) ,ever_list[8]))


        gerenhuizong.append(count_pingshi)
        gerenhuizong.append(count_zhoumo)
        gerenhuizong.append(count_chidao)
        huizong = ("总计： 姓名：%s  平时加班时长：%.2f  周末加班时长：%.2f  迟到次数: %d" %(name , gerenhuizong[0] ,gerenhuizong[1],gerenhuizong[2]))

def panduanriqi_loudaka(_last_data, _config):
    honban = []
    for every_data in _last_data:
        date = every_data[3]
        if is_holiday(date , _config) or is_weekend(date ,_config):
            every_data.append("假期")
        else:
            every_data.append("上班")

        del every_data[0]
        every_data.append('0') #增加普通加班列
        every_data.append('0') #增加周末加班列
        every_data.append('0') #增加迟到时间列
        #判断平时上班还是周末，计算平时加班，计算周末加班，判断迟到时长

        if every_data[5] == '上班':
            #判断迟到
            if chidao(every_data[3]) is not None:
                every_data[8] = chidao(every_data[3])
            else:pass
            #判断漏打卡,若无漏打卡计算加班时间;若有上班漏打卡计算加班时间 下班漏打卡提示and旷工提示
            if loudaka(every_data[3],every_data[4]) == '':
                every_data[6] = shijiancha("17:30:00" ,every_data[4])

            elif loudaka(every_data[3],every_data[4]) == 'shang':
                every_data[6] = shijiancha("17:30:00" ,every_data[4])

            elif loudaka(every_data[3],every_data[4]) == 'xia':
                pass

            elif loudaka(every_data[3],every_data[4]) == 'kuang':
                pass

            else:
                pass

        elif every_data[5] == '假期':
            every_data[7] = shijiancha(every_data[3],every_data[4])

        honban.append(every_data)
        #every_data[6]是平时加班小时数  every_data[7]是周末节假日加班小时数 every_data[8]是迟到时长
    return honban


#通过相同的姓名和相同的日期合并打卡数据
def data_merge(_all_in):
    last_all = []
    for i in _all_in:
        if not i[1].strip() == '':
            haveID = i
        else:
            continue
        #这里把标杆的带工号的haveID 取出来 每个haveID都带工号
        #================================================
        #下边的for循环中don为从_all_in 取出的每个值。然后再去和每个带工号的haveID标杆做比较
        for don in _all_in:
            if haveID[2] == don[2] and haveID[3] == don[3]:
                #开始判断上班时间
                #判断haveID[4]上班时间的值为空 and don[4] 也为空
                if haveID[4].strip() == '' and don[4].strip() == '':
                    pass
                #判断haveID[4]上班时间的值为空， don[4] 不为空
                elif haveID[4].strip() == '' and not don[4].strip() == '':
                    haveID[4] = don[4]

                #判断haveID[4]上班时间的值不为空， don[4]值为空
                elif not haveID[4].strip() == '' and don[4].strip() == '':
                    pass

                #判断haveID[4]上班时间的值不为空， don[4]值为不为空
                elif not haveID[4].strip() == '' and not don[4].strip() == '':
                    time1 = datetime.datetime.strptime(haveID[4] , '%H:%M:%S')
                    time2 = datetime.datetime.strptime(don[4] , '%H:%M:%S')
                    if (time1 < time2):
                        pass
                    elif (time1 > time2):
                        haveID[4] = don[4]
                    else:
                        pass

                #开始判断下班时间
                #判断haveID[5]下班时间的值为空 and don[5] 也为空
                if haveID[5].strip() == '' and don[5].strip() == '':
                    pass
                #判断haveID[5]下班时间的值为空， don[5] 不为空 则don[5]赋值给haveID[5]
                elif haveID[5].strip() == '' and not don[5].strip() == '':
                    haveID[5] = don[5]

                #判断haveID[5]下班时间的值不为空， don[5]值为空
                elif not haveID[5].strip() == '' and don[5].strip() == '':
                    pass

                #判断haveID[5]下班时间的值不为空， don[5]值为不为空  则比较时间保留较大的那个时间
                elif not haveID[5].strip() == '' and not don[5].strip() == '':
                    time1 = datetime.datetime.strptime(haveID[5] , '%H:%M:%S')
                    time2 = datetime.datetime.strptime(don[5] , '%H:%M:%S')
                    if (time1 < time2):
                        haveID[5] = don[5]
                    elif (time1 > time2):
                        pass
                    else:
                        pass

            else:
                continue
        last_all.append(haveID)
        #print (haveID)
    return last_all
        


#判断漏打卡
def loudaka(_shangban ,_xiaban):
    flog = ''
    if (_shangban.strip() == '' and not _xiaban.strip() == ''):
        flog = 'shang'
        #print (_userName, ":   于", _date ,"上班打卡时间：" ,_shangban ,"下班打卡时间：" ,_xiaban ,"上班漏打卡！！")
        return flog
    elif (not _shangban.strip() == '' and _xiaban.strip() == ''):
        flog = 'xia'
        #print (_userName, ":   于", _date ,"上班打卡时间：" ,_shangban ,"下班打卡时间：" ,_xiaban ,"下班漏打卡！！")
        return flog
    elif (_shangban.strip() == '' and _xiaban.strip() == ''):
        flog = 'kuang'
        #print ("上下班都没打卡....旷工")
        return flog

    return flog


#计算加班时间  开始是开始加班的时间   结束时结束加班的时间
def shijiancha(kaishi ,jieshu):
    if (not kaishi.strip()  == '' and not jieshu.strip() == ''):
        time_start = datetime.datetime.strptime(kaishi , '%H:%M:%S')
        time_end   = datetime.datetime.strptime(jieshu , '%H:%M:%S')
        if (time_start > time_end):
            return str(0)
        times = str((time_end - time_start)).split(":")

        hour = float(times[0])

        minute = float(times[1])

        if (hour < 1):     #总加班时间不满一小时不算加班
            return str(0)

        jiaban_time = ('%.1f' % (float(hour) + float(minute) / 60))
        jiaban_time = judgeNUM(jiaban_time)    #判断小数点后一位
        return jiaban_time
    else:
        return str(0)

#查看早上上班是否迟到
def chidao(_shangban ,work_time = '09:00:00'):
    if (not _shangban.strip() == ''):
        _shangban = datetime.datetime.strptime(_shangban , '%H:%M:%S')
        work_time = datetime.datetime.strptime(work_time , '%H:%M:%S')
        if (_shangban <= work_time):
            pass
            #print (_shangban,"没有迟到")
        elif (_shangban > work_time):
            late_time = str((_shangban - work_time)).split(":")  #late_time 是迟到时间

            hour = late_time[0]
            minute = late_time[1]
            second = late_time[2]

            return(hour + ':' + minute + ':' + second)
        else:
            pass
    else:
        pass

#判断是否为周末
def is_weekend(_date ,_config):
    flag = False
    riqi = _date[0:10]  #日期
    xingqi = _date[11]   #星期几
    The_workday = _config.get('day' , 'workday')  #工作日配置文件
    if (xingqi == '六' or xingqi =='日') and (not riqi in The_workday):
        flag = True
    else:
        flag = False

    return flag   #如果return _date  会是什么结果？

#########################
#只要不是周末 ，或者节假日 都是上班的日子
#########################

#判断是否为节假日
def is_holiday(_date , _config):
    flag = False
    _date = _date[0:10]
    The_holiday = _config.get('day' , 'holiday')
    if (_date in The_holiday):
        #print (_date, "是假期")
        flag = True
        return flag
    else:
        #print (_date, "不是假期哟")
        return flag

#获取配置文件把节假日等不可控日期写在配置文件中
def get_config():
    config = configparser.ConfigParser()
    config_file = open('Myfirst.ini')
    config.readfp(config_file)
    config_file.close()

    return config

#处理上下班时间
def chuli_time(lie_time):
    #把 9:28:03 变成 09:28:03 因为try中只处理float的数据所以 直接的str时间也需要在except中增加处理
    #使用replace(' ' , '')去除中间空格
    try:
        float(lie_time)
        new_time = float(lie_time)
        new_time = xlrd.xldate_as_tuple(new_time ,0)
        d = new_time[3]
        if (d < 10):
            d = '0' + str(d)
        else:
            d = str(new_time[3])
        e = new_time[4]
        if (e < 10):
            e = '0' + str(e)
        else:
            e = str(new_time[4])
        f = new_time[5]
        if (f < 10):
            f = '0' + str(f)
        else:
            f = str(new_time[5])
        return (d + ":" + e + ":" + f)
    except:
        if (lie_time == ''):        #判断传入空字符串直接退出方法
            return lie_time
        lie_time = lie_time.replace(' ' ,'')
        (a,b,c) = lie_time.split(':')
        if (int(a) < 10):
            a = '0' + a
        if (int(b) < 10):
            b = '0' + b
        if (int(c) < 10):
            c = '0' + c
        return (a + ":" + b + ":" + c)
        #return lie_time
        #return 1

#删除部门班组上班描述下班描述迟到分钟早退分钟加班小时旷工[天]	未刷次数
def geshihuashuju(zhongzhuan_in):

        del zhongzhuan_in[0]     #删除所属部门
        del zhongzhuan_in[5]     #
        for m in range(6):    #循环六次删除不需要的值
            del zhongzhuan_in[6]

        return 1

def judgeNUM(_num):
    if '.' in _num:
        _num = str(_num)
        (zheng , fen) = _num.split('.')
        if int(fen)>= 5:
            fen = str(5)
        elif int(fen) < 5:
            fen = str(0)
        _num = float(zheng + '.' + fen)
        return _num
    else:
        return _num


if __name__ == "__main__":
    main()

