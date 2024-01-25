"""
抓取民政部网站最新行政区划代码
"""

import requests
from lxml import etree
import re
from hashlib import md5
import redis
import sys

class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
        # 建立redis连接
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def get_html(self, url):
        """功能函数1 - 获取html"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def xpath_func(self, html, xpath_bds):
        """功能函数2 - xpath解析提取数据"""
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)

        return r_list

    def md5_url(self, url):
        """功能函数3 - 对URL地址进行md5加密生成指纹"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def parse_html(self):
        """爬虫逻辑函数"""
        # 1、向主页发请求,提取最新月份的链接
        # 2、向最新月份链接发请求,来提取具体的数据
        one_html = self.get_html(url=self.url)
        one_xpath = '//table/tr[2]/td[2]/a/@href'
        href_list = self.xpath_func(html=one_html, xpath_bds=one_xpath)
        if href_list:
            one_url = 'http://www.mca.gov.cn' + href_list[0]
            finger = self.md5_url(one_url)
            # 返回值为1,说明添加到集合成功,也就是之前没有抓取过
            if self.r.sadd('mzb:spiders', finger) == 1:
                # 获取具体数据
                self.detail_page(one_url)
            else:
                sys.exit('数据更新完成')
        else:
            print('提取最新链接失败')

    def detail_page(self, one_url):
        """详情页：获取具体数据"""
        # 响应内容中嵌入JS,进行了URL地址的跳转
        # 从响应内容two_html中提取真实返回数据的链接
        two_html = self.get_html(url=one_url)
        true_url = self.get_true_url(two_html)
        # 开始从真实链接中提取具体的数据
        true_html = self.get_html(url=true_url)
        two_xpath = '//tr[@height="19"]'
        tr_list = self.xpath_func(html=true_html, xpath_bds=two_xpath)
        print(tr_list)
        item = {}
        for tr in tr_list:
            item['name'] = tr.xpath('./td[3]/text()')[0].strip()
            item['code'] = tr.xpath('./td[2]/text() | ./td[2]/span/text()')[0].strip()
            print(item)

    def get_true_url(self, two_html):
        """从响应内容中提取真实返回数据的URL地址"""
        regex = 'window.location.href="(.*?)"'
        pattern = re.compile(regex, re.S)

        return pattern.findall(two_html)[0]

    def run(self):
        """程序入口函数"""
        self.parse_html()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()

























