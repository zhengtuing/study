# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KfcItem(scrapy.Item):
    # 门店编号  门店名称 门店地址  所属城市  所属省份
    rownum = scrapy.Field()
    storeName = scrapy.Field()
    addressDetail = scrapy.Field()
    cityName = scrapy.Field()
    provinceName = scrapy.Field()












