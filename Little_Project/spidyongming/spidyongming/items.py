# -*- coding: utf-8 -*-
#定义我们需要获取的字段
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidyongmingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
    定义我要提取内容的字段名字
    '''
    name = scrapy.Field()
    #小说的名字
    author = scrapy.Field()
    #作者
    novelurl = scrapy.Field()
    #小说地址
    serialstatus = scrapy.Field()
    #状态
    serialnumber = scrapy.Field()
    #连载字数
    category = scrapy.Field()
    #文章类别
    name_id = scrapy.Field()
    #小说编号

