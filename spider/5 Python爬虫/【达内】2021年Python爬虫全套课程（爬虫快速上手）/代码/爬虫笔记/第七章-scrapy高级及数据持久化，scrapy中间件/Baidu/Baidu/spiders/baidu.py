# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名,执行爬虫时使用: scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬取的域名: scrapy genspider baidu www.baidu.com
    allowed_domains = ['www.baidu.com']
    # 起始的URL地址
    start_urls = ['http://www.baidu.com/']

    # 解析提取数据的函数
    def parse(self, response):
        """解析提取数据 - 百度一下,你就知道"""
        item = {}
        # response.xpath()结果: [<selector xpath='' data='xxxx'>]
        # extract()结果: ['百度一下,你就知道']
        # extract_first()结果: '百度一下,你就知道'
        # get()结果: '百度一下,你就知道'  等同于extract_first()
        item['title'] = response.xpath('/html/head/title/text()').get()
        print(item)
