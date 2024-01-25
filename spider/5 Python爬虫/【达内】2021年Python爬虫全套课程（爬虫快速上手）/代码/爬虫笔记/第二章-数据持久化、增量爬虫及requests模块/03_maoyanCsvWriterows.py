"""
猫眼电影top100抓取
"""

from urllib import request
import re
import time
import random
import csv

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 添加计数变量
        self.i = 0
        # 打开文件,并初始化写入对象
        self.f = open('maoyan.csv','a',newline='')
        self.writer = csv.writer(self.f)
        # 定义空列表,用来存储所有电影信息的大列表
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
            # 每个电影的信息处理之后添加到总列表中
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
        # 所有页所有数据抓取完成后,进行writerows()数据写入
        self.writer.writerows(self.all_film_list)
        self.f.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
    print('电影数量:',spider.i)













