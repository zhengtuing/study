# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    i = 1
    start_urls = ['https://www.guazi.com/langfang/buy/o1/#bread']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 给items.py中的GuaziItem类做实例化
            item = GuaziItem()
            item['name'] = li.xpath('./a/h2/text()').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['link'] = li.xpath('./a/@href').get()

            # 把抓取的数据提交给管道文件处理: yield item
            yield item

        # 生成下一页的地址,去交给调度器入队列
        if self.i < 5:
            self.i += 1
            url = 'https://www.guazi.com/langfang/buy/o{}/#bread'.format(self.i)
            # 把url交给调度器入队列
            yield scrapy.Request(url=url, callback=self.parse)