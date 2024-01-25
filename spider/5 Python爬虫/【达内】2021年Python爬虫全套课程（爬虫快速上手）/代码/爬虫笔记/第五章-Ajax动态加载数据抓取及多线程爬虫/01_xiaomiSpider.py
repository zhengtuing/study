"""
抓取小米应用商店中：聊天社交类别下的应用信息
具体数据：
    1、应用名称
    2、应用链接
    3、应用类别
"""
import requests
import time
import random
from fake_useragent import UserAgent

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'

    def get_html(self, url):
        """请求获取响应内容html"""
        headers = { 'User-Agent' : UserAgent().random }
        # 此处使用 .json() ，直接获取python数据类型
        html = requests.get(url=url, headers=headers).json()
        self.parse_html(html)

    def parse_html(self, html):
        """解析函数"""
        item = {}
        for app_dict in html['data']:
            item['name'] = app_dict['displayName']
            item['type'] = app_dict['level1CategoryName']
            item['link'] = 'http://app.mi.com/details?id=' + app_dict['packageName']
            print(item)

    def run(self):
        total = self.get_total()
        for page in range(total):
            url = self.url.format(page)
            self.get_html(url=url)
            time.sleep(random.randint(1,2))

    def get_total(self):
        """获取总页数"""
        page_url = 'http://app.mi.com/categotyAllListApi?page=0&categoryId=2&pageSize=30'
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=page_url, headers=headers).json()
        count = html['count']
        total = count//30 if count%30==0 else count//30 + 1

        return total

if __name__ == '__main__':
    spider = XiaomiSpider()
    spider.run()












