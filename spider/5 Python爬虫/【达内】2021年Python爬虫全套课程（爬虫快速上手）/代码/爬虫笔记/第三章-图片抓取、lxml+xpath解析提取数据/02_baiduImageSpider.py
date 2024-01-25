"""
抓取指定关键字的,百度图片首页的30张图片
"""
import requests
import re
import time
import random
import os
from urllib import parse

class BaiduImageSpider:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        self.word = input('请输入关键字:')
        self.i = 1
        self.directory = './images/{}/'.format(self.word)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def parse_html(self):
        """数据抓取函数"""
        params = parse.quote(self.word)
        html = requests.get(url=self.url.format(params),headers=self.headers).text
        regex = 'thumbURL":"(.*?)"'
        pattern = re.compile(regex,re.S)
        src_list = pattern.findall(html)
        # src_list : ['http://xx.jpg','http://xx.jpg']
        for src in src_list:
            # 函数功能：保存1张图片到本地
            self.save_image(src)

    def save_image(self, src):
        """保存1张图片到本地"""
        html = requests.get(url=src,headers=self.headers).content
        # filename : ./images/赵丽颖/赵丽颖_1.jpg
        filename = self.directory + '{}_{}.jpg'.format(self.word,self.i)
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')
        self.i += 1

    def run(self):
        """程序入口函数"""
        self.parse_html()

if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()












