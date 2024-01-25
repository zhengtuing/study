# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'

    def start_requests(self):
        """生成所有页要抓取的URL地址,一次性交给调度器入队列"""
        for sn in range(30, 151, 30):
            page_url = self.url.format(sn)
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        """提取图片链接"""
        html = json.loads(response.text)
        for one_image_dict in html['list']:
            item = SoItem()
            item['image_url'] = one_image_dict['qhimg_url']
            item['image_title'] = one_image_dict['title']

            # 图片链接提取完成后,直接交给管道文件处理即可
            yield item










