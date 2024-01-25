# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['www.guazi.com']
    # 1. 删掉start_urls变量
    # 2. 重写start_requests()方法
    def start_requests(self):
        """一次性生成所有要抓取的URL地址,一次性交给调度器入队列"""
        for i in range(1, 6):
            url = 'https://www.guazi.com/langfang/buy/o{}/#bread'.format(i)
            # 交给调度器入队列,并指定解析函数
            yield scrapy.Request(url=url, callback=self.detail_page)

    def detail_page(self, response):
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 给items.py中的GuaziItem类做实例化
            item = GuaziItem()
            item['name'] = li.xpath('./a/h2/text()').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['link'] = li.xpath('./a/@href').get()

            # 把抓取的数据提交给管道文件处理: yield item
            yield item
