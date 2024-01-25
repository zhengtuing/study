"""
建立免费代理IP池 - 西刺代理（国内高匿代理）
"""
import requests
from lxml import etree
import time
import random

class ProxyPool:
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/{}'
        self.test_url = 'http://www.baidu.com/'
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    def get_proxy_pool(self, url):
        html = requests.get(url=url, headers=self.headers).text
        p = etree.HTML(html)
        # 1、基准xpath
        tr_list = p.xpath('//table[@id="ip_list"]/tr')
        for tr in tr_list[1:]:
            ip = tr.xpath('./td[2]/text()')[0].strip()
            port = tr.xpath('./td[3]/text()')[0].strip()
            # 测试代理IP是否可用
            self.test_proxy(ip, port)

    def test_proxy(self, ip, port):
        """测试一个代理IP是否可用"""
        proxies = {
            'http' : 'http://{}:{}'.format(ip,port),
            'https': 'https://{}:{}'.format(ip, port)
        }
        try:
            res = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=2)
            if res.status_code == 200:
                print(ip,port,'\033[31m可用\033[0m')
                # 把此IP保存到文件
                with open('proxy.txt', 'a') as f:
                    f.write(ip + ':' + port + '\n')
        except Exception as e:
            print(ip,port,'不可用')

    def run(self):
        for i in range(1, 1001):
            url = self.url.format(i)
            self.get_proxy_pool(url=url)

if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()








