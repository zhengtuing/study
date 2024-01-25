"""
汽车之家数据抓取 - 两级页面
"""
from urllib import request
import re
import time
import random

class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 计数变量
        self.i = 0

    def get_html(self,url):
        """功能函数1：获取响应内容"""
        req = request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        # 知识点1： ignore: decode()时遇到不能识别的字符,则忽略掉
        # 知识点2： decode()时,如果出现乱码,则去查看网页的字符编码是什么
        html = res.read().decode('gb2312','ignore')

        return html

    def re_func(self, regex, html):
        """功能函数2：解析提取数据"""
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_html(self, one_url):
        """数据抓取函数 - 从一级页面解析开始"""
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        # href_list: ['/declear/xxxx/xxx/xx','/declear/xxxx/xxx/xx','']
        href_list = self.re_func(one_regex,one_html)
        for href in href_list:
            # 汽车详情页需要拼接
            car_url = 'https://www.che168.com' + href
            self.get_data(car_url)
            # 抓取1辆汽车的信息,随机休眠1-2秒钟,uniform()生成指定范围的浮点数
            time.sleep(random.uniform(1,3))

    def get_data(self, car_url):
        """功能：抓取1辆汽车的详情数据"""
        two_html = self.get_html(car_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b>.*?</div>'
        # car_list: [('天籁 2016款 改款 2.0L XL舒适版','2万公里','2018年02月','自动 / 2L','廊坊','14.99'),]
        car_list = self.re_func(two_regex,two_html)
        item = {}
        item['name'] = car_list[0][0].strip()
        item['km'] = car_list[0][1].strip()
        item['time'] = car_list[0][2].strip()
        item['type'] = car_list[0][3].split('/')[0].strip()
        item['displace'] = car_list[0][3].split('/')[1].strip()
        item['city'] = car_list[0][4]
        item['price'] = car_list[0][5]

        print(item)

    def run(self):
        """程序入口函数"""
        for i in range(1,3):
            url = self.url.format(i)
            self.parse_html(url)

if __name__ == '__main__':
    spider = CarSpider()
    spider.run()
























