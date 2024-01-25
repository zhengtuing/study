# -*- coding: utf-8 -*-
import scrapy
from ..items import PptItem

class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/']

    def parse(self, response):
        """一级页面解析函数,提取数据: 29个分类名称+链接"""
        print(response.text)
        li_list = response.xpath('//div[@class="col_nav i_nav clearfix"]/ul[3]/li')
        for li in li_list[1:]:
            item = PptItem()
            item['class_name'] = li.xpath('./a/text()').get()
            class_href = 'http://www.1ppt.com' + li.xpath('./a/@href').get()

            # 将class_href交给调度器入队列
            yield scrapy.Request(url=class_href, meta={'meta1':item}, callback=self.parse_second_page)

    def parse_second_page(self, response):
        """二级页面解析函数,提取数据：PPT名称 和 进入PPT详情页链接"""
        # 接收上一个解析函数中传递过来的item对象
        meta1 = response.meta['meta1']
        # 开始提取数据(20个PPT)
        li_list = response.xpath('//ul[@class="tplist"]/li')
        for li in li_list:
            item = PptItem()
            item['ppt_name'] = li.xpath('./h2/a/text()').get()
            item['class_name'] = meta1['class_name']
            ppt_info_url = 'http://www.1ppt.com' + li.xpath('./h2/a/@href').get()

            # 交给调度器入队列
            yield scrapy.Request(url=ppt_info_url, meta={'meta2':item}, callback=self.parse_third_page)

    def parse_third_page(self, response):
        """三级页面解析函数,提取数据: 进入下载页面的链接"""
        meta2 = response.meta['meta2']
        enter_download_page = 'http://www.1ppt.com' + response.xpath('//ul[@class="downurllist"]/li/a/@href').get()
        # 直接交给调度器入队列
        yield scrapy.Request(url=enter_download_page, meta={'item':meta2}, callback=self.parse_forth_page)

    def parse_forth_page(self, response):
        """四级页面解析函数,提取数据: 具体PPT的下载链接"""
        item = response.meta['item']
        item['ppt_download_url'] = response.xpath('//ul[@class="downloadlist"]/li[1]/a/@href').get()

        # 至此,1条完整的item数据提取完成,交给管道文件处理
        yield item














