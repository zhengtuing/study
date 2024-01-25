# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道1 : 终端打印输出
class GuaziPipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['price'])
        return item

# 管道2 : 存入MySQL数据库
# 提前建库建表
# create database guazidb charset utf8;
# use guazidb;
# create table guazitab(
# name varchar(200),
# price varchar(100),
# link varchar(300)
# )charset=utf8;
import pymysql
from .settings import *

class GuaziMysqlPipeline(object):
    def open_spider(self, spider):
        """爬虫程序开始时,只执行一次,一般用于数据库的连接"""
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()
        print('我是open_spider函数')

    def process_item(self, item, spider):
        ins = 'insert into guazitab values(%s,%s,%s)'
        li = [
            item['name'].strip(),
            item['price'].strip(),
            item['link'].strip()
        ]
        self.cur.execute(ins, li)
        # 千万不要忘记提交到数据库执行
        self.db.commit()

        return item

    def close_spider(self, spider):
        """爬虫程序结束时,只执行一次,一般用于数据库的断开"""
        self.cur.close()
        self.db.close()
        print('我是close_spider函数')

# 管道3 - 存入MongoDB数据库管道
import pymongo

class GuaziMongoPipeline(object):
    def open_spider(self, spider):
        """连接mongodb"""
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = dict(item)
        self.myset.insert_one(d)

        return item











