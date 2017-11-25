#coding:utf-8
# -*- coding: utf-8 -*-
#逆转字符串——输入一个字符串，将其逆转并输出。

'''
知识点
========================================================
利用了列表的切片
li = "dondake"
lala = li[:]     #输出[dondake]，省略起始索引、终止索引、步长值表示取全部，
lala = li[::]    #输出[dondake]，省略起始索引、终止索引、步长值表示取全部，
lala = li[::-1]  ##输出[ekadnod]，省略起始索引、终止索引，步长值为-1，表示反向获取,反向获取全部
'''

def main():
    shuru = input("请输入需要转换的内容：")
    shuchu = nizhuan1(shuru)
    #shuchu = nizhuan2(shuru)
    #print (shuchu)

    return shuchu


def nizhuan1(_shuru):
    return (_shuru[::-1])


def nizhuan2(_shuru):
    li = list(_shuru)
    li.reverse()
    #reverse() 函数用于反向列表中元素。
    rt = "".join(li)
    return (rt)



if __name__ == "__main__":
    dondake = main()
    print (dondake)