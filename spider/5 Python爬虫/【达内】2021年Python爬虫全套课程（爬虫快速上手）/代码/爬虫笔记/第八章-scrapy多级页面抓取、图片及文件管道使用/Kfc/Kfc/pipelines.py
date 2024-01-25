# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KfcPipeline(object):
    def process_item(self, item, spider):
        return item

# 管道2 - 数据持久化到MySQL数据库
import pymysql

class KfcMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect('localhost', 'root', '123456', 'kfcdb', charset='utf8')
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into kfctab values(%s,%s,%s,%s,%s)'
        li = [
            item['rownum'],
            item['storeName'],
            item['addressDetail'],
            item['cityName'],
            item['provinceName'],
        ]
        self.cur.execute(ins, li)
        self.db.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()






# create database kfcdb charset utf8;
# use kfcdb;
# create table kfctab(
# rownum varchar(100),
# storeName varchar(100),
# addressDetail varchar(100),
# cityName varchar(100),
# provinceName varchar(100)
# )charset=utf8;









