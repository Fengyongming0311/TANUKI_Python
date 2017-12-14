# -*- coding: utf-8 -*-
#定义我们的存储
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidyongmingPipeline(object):
    def process_item(self, item, spider):
        return item
