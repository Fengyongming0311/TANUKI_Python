#coding:utf-8


import xlrd

def main():
    #print 'dondake',u"冯泳铭从0到1 是最困难的！！！"
    data = xlrd.open_workbook('TestFYM.xls') #打开文件
    #print type(data)
    bak = unicode(data.sheet_names())   #查看有多少个表
    #print type(bak)   #type为list
    print bak
    print bak.decode('raw_unicode_escape') #打印出来表名
    '''
    table1 = data.sheets()[0]    #把第一个表赋值给table1
    print table1

    biao1_bak = data.sheet_by_index(0) #通过索引 找到表1
    print biao1_bak
    '''
    biao1 = data.sheet_by_name(u'总览')  #通过表名找到这个表1！
    print biao1

    print u"表名为:",biao1.name,u"表中有多少行:",biao1.nrows,u"表中有多少列:",biao1.ncols  #sheet的名称，行数，列数

    henghang = biao1.row_values(0)   # 这是第一行表头
    print henghang

    lie = biao1.col_values(3)



    print "==================================================="
    '''
    print biao1.cell(21,5).value.encode('GBK')  #读取指定的行
    print biao1.cell_value(21,5).encode("GBK")  #第二种方法
    print biao1.row(21)[5].value.encode("GBK")  #第三种方法



    print biao1.cell(21,4).ctype   #单元格数据类型
    #返回5种类型：0 empty;1 string;2 number;3 date;4 boolean;5 error
    '''
    print biao1.row(21)[4].value.encode("GBK")  #第三种方法






if __name__ == "__main__":
    main()
