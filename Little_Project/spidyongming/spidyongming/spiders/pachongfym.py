__author__ = 'TANUKI'
#coding:utf-8
import re
import scrapy
from bs4 import BeautifulSoup
import sys
sys.path.append('..')
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from items import SpidyongmingItem ##这是我定义的需要保存的字段，（导入spidyongming项目中，items文件中的SpidyongmingItem类）

class Myspider(scrapy.Spider):

    name = 'dingdian'
    #这name就是我们在entrypoint.py文件中的第三个参数！
    allowed_domains = ['x23us.com']
    #这个不是必须的，但在某些情况下需要用得到，
    #比如使用爬取规则的时候就需要了；它的作用是只会跟进存在于allowed_domains中的URL。不存在的URL会被忽略。
    bash_url = 'http://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        #yield Request('http://www.23wx.com/quanben/1', self.parse)