"""
xpath提取猫眼电影top100
"""
import requests
from lxml import etree
import time
import random

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html(html)

    def parse_html(self, html):
        """xpath提取数据"""
        p = etree.HTML(html)
        item = {}
        # 1、基准xpath：匹配每个电影信息的 dd 节点对象列表
        #    dd_list: [<element dd at xxx>,<element dd at xxx>,...]
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/@title')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            item['url'] = 'https://maoyan.com' + dd.xpath('.//p[@class="name"]/a/@href')[0].strip()
            item['score'] = ''.join(dd.xpath('.//p[@class="score"]/i/text()'))
            print(item)

    def run(self):
        for i in range(0,91,10):
            url = self.url.format(i)
            self.get_html(url)
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()













