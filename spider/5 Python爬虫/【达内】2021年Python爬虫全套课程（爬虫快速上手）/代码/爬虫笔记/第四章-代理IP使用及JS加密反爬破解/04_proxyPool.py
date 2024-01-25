"""
建立自己的代理IP池 - 开放代理
"""
import requests

class ProxyPool:
    def __init__(self):
        self.proxy_url = 'http://dev.kdlapi.com/api/getproxy/?orderid=918685340630466&num=20&protocol=1&method=2&an_an=1&an_ha=1&sep=2'
        self.test_url = 'http://www.baidu.com/'
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    def get_proxy_pool(self):
        html = requests.get(url=self.proxy_url, headers=self.headers).text
        proxy_list = html.split('\n')
        # for循环遍历,依次对每个代理IP进行测试是否可用
        for proxy in proxy_list:
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        """测试一个代理IP是否可用"""
        # proxy: 1.1.1.1:8888
        proxies = {
            'http' : 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy)
        }
        try:
            res = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=2)
            if res.status_code == 200:
                print(proxy,'\033[31m可用\033[0m')
        except Exception as e:
            print(proxy,'不可用')

    def run(self):
        self.get_proxy_pool()

if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()








