# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
from bs4 import BeautifulSoup
from scrapy.http import Request
from chinanews_spider.items import ChinanewsSpiderItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.chinanews.com']
    #base_url = 'http://channel.chinanews.com/cns/s/channel:life.shtml?pager=1&pagenum=20'
    base_url = 'http://channel.chinanews.com/cns/s/channel:{ctgy}.shtml?pager={pager}&pagenum=20'
    #ctgys = ['yl', 'ty']
    ctgys = ['ty', 'yl', 'cj', 'mil', 'auto', 'gj', 'it', 'sh']
    pagers = range(1, 5000) 

    def start_requests(self):
        for ctgy in self.ctgys:
            for pager in self.pagers:
                url = self.base_url.format(ctgy=ctgy, pager=pager)
                #time.sleep(0.03)
                yield Request(url, self.parse)

    def parse(self, response):
        #print(response.text)
        temp = response.text
        handle = temp.split('docs\" :')[1].split('};')[0]
        results = json.loads(handle)
        #print(results)
        item = ChinanewsSpiderItem()
        for result in results:
            Check = result['url'].split('/')[3]
            print(Check)
            if Check in self.ctgys:
                item['category'] = Check
                item['content'] = result['content']
            #print(item['category'], item['content'])
            yield item
