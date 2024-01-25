# -*- coding: utf-8 -*-
import scrapy
from ..items import BaixiaoduItem

class BaixiaoduSpider(scrapy.Spider):
    name = 'baixiaodu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        item = BaixiaoduItem()
        item['title'] = response.xpath('/html/head/title/text()').get()
        print('我是parse函数的输出')

        yield item
