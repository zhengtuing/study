"""
抓取豆瓣电影数据
"""
import requests
import json
import time
import random
from fake_useragent import UserAgent
import re

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        # 存入json文件
        self.f = open('douban.json', 'w', encoding='utf-8')
        self.item_list = []

    def get_agent(self):
        """功能函数1 - 获取随机User-Agent"""
        return UserAgent().random

    def get_html(self, url):
        """功能函数1 - 获取html"""
        html = requests.get(url=url, headers={'User-Agent':self.get_agent()}).text

        return html

    def parse_html(self, url):
        """爬虫解析函数"""
        # json.loads() 把json格式的字符串转为python数据类型 html：[{},{},{},{}]
        html = json.loads(self.get_html(url=url))
        item = {}
        for one_film in html:
            item['name'] = one_film['title']
            item['score'] = one_film['score']
            item['rank'] = one_film['rank']
            item['time'] = one_film['release_date']
            print(item)
            # 把每个电影的字典添加到大列表中,用于最后的json.dump()
            self.item_list.append(item)

    def run(self):
        """程序入口函数"""
        # 字典：{'剧情':'11','爱情':'13','喜剧':'5',....}
        type_dict = self.get_type_dict()
        menu = ''
        for t in type_dict:
            menu = menu + t + '|'
        print(menu)
        choice = input('请输入电影类别：')
        typ = type_dict[choice]
        # 获取电影总数量
        total = self.get_total(typ)
        for start in range(0,total,20):
            url = self.url.format(typ, start)
            self.parse_html(url=url)
            time.sleep(random.randint(1,2))
        # 所有的数据抓取完成后,存入到本地的json文件
        json.dump(self.item_list, self.f, ensure_ascii=False)
        self.f.close()

    def get_type_dict(self):
        """获取所有类别的字典"""
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url=url)
        regex = '<span><a href=".*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action=">'
        pattern = re.compile(regex, re.S)
        # r_list: [('剧情','11'),('喜剧','5'),('爱情':'13),...]
        r_list = pattern.findall(html)
        type_dict = {}
        for r in r_list:
            type_dict[r[0]] = r[1]

        return type_dict

    def get_total(self, typ):
        """获取某个类别下的电影总数量"""
        page_url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(typ)
        html = json.loads(self.get_html(url=page_url))

        return html['total']

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()








