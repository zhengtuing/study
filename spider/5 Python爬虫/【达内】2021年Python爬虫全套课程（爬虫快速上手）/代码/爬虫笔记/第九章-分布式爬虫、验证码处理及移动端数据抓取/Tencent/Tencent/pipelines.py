# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):
    def process_item(self, item, spider):
        return item

import pymysql
from .settings import *

class TencentMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into tencenttab values(%s,%s,%s,%s,%s,%s)'
        li = [
            item['job_name'],
            item['job_address'],
            item['job_type'],
            item['job_time'],
            item['job_responsibility'],
            item['job_requirement'],
        ]
        self.cur.execute(ins, li)
        self.db.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()







