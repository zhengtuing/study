"""
猫眼电影top100抓取
"""

from urllib import request
import re
import time
import random
import pymongo

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 添加计数变量
        self.i = 0
        # 连接对象 + 库对象 + 集合对象
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['maoyanset']

    def get_html(self,url):
        """获取响应内容"""
        req = request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        """解析函数"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex,re.S)
        # r_list: [('霸王别姬','张国荣','1993'),(),(),()]
        r_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self,r_list):
        """数据处理函数"""
        for r in r_list:
            # 存入mongodb,item字典必须定义到for循环里面,让每个电影都会自动生成一个新的id,作为文档中的 id 字段
            item = {}
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            # 存入mongodb数据库 - 1条1条存入
            self.myset.insert_one(item)
            print(item)
            self.i += 1

    def run(self):
        """程序入口函数"""
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 控制数据抓取频率
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
    print('电影数量:',spider.i)













