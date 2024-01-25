# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # 定义数据结构依据：管道文件数据处理时你需要哪些数据
    # 最终需要的数据： ./novel/盗墓笔记1:七星鲁王宫/七星鲁王_第一章_血尸.txt
    parent_title = scrapy.Field()
    son_title = scrapy.Field()
    novel_content = scrapy.Field()















