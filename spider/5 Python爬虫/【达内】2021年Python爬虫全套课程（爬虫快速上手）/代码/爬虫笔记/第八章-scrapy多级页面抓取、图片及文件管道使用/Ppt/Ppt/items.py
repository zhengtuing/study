# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
    # 定义什么?? 管道文件需要什么?
    class_name = scrapy.Field()
    ppt_name = scrapy.Field()
    ppt_download_url = scrapy.Field()

