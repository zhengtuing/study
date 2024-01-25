"""
猫眼电影top100抓取 - excutemany()
"""

from urllib import request
import re
import time
import random
import pymysql

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 添加计数变量
        self.i = 0
        # 数据库连接对象 + 游标对象 + 存放所有电影信息的大列表
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        self.cursor = self.db.cursor()
        self.all_film_list = []

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
            film_t = (
                r[0].strip(),
                r[1].strip(),
                r[2].strip()
            )
            # 把所有电影的元组添加到大列表中,用于最后的 executemany()
            self.all_film_list.append(film_t)
            print(film_t)
            self.i += 1

    def run(self):
        """程序入口函数"""
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 控制数据抓取频率
            time.sleep(random.randint(1,2))
        # 所有数据抓取完成,一次性存入到MySQL数据库
        ins = 'insert into maoyantab values(%s,%s,%s)'
        self.cursor.executemany(ins,self.all_film_list)
        self.db.commit()
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
    print('电影数量:',spider.i)













