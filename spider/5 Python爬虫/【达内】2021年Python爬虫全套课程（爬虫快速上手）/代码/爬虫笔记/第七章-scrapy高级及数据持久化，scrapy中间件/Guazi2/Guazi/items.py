# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # 汽车名称、价格、链接
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    # 行驶里程、排量、变速箱
    km = scrapy.Field()
    displacement = scrapy.Field()
    typ = scrapy.Field()


# 相当于你定义了一个字典,只给了Key,没有给Value
# {'name':'', 'price':'', 'link':''}
