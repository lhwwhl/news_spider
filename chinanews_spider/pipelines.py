# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .sql import Sql
from chinanews_spider.items import ChinanewsSpiderItem

print('开始执行pipeline')
class ChinanewsSpiderPipeline(object):
    def process_item(self, item, spider):
        print('开始执行pipeline')
        if isinstance(item, ChinanewsSpiderItem):
            category = item['category']
            content = item['content']
            Sql.insert_news(category, content)
            print('开始存入数据')
