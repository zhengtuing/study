"""
多线程抓取小米应用商店的应用信息
"""
import requests
import time
from threading import Thread,Lock
from queue import Queue
from fake_useragent import UserAgent

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        # 创建队列
        self.q = Queue()
        self.lock = Lock()

    def url_in(self):
        """将URL地址入队列"""
        for page in range(67):
            url = self.url.format(page)
            # 入队列
            self.q.put(url)

    def parse_html(self):
        """线程事件函数: 获取URL,请求,解析,处理数据"""
        while True:
            # 上锁
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                # 释放锁
                self.lock.release()
                headers = { 'User-Agent' : UserAgent().random }
                html = requests.get(url=url, headers=headers).json()
                item = {}
                for app_dict in html['data']:
                    item['name'] = app_dict['displayName']
                    item['type'] = app_dict['level1CategoryName']
                    item['link'] = 'http://app.mi.com/details?id=' + app_dict['packageName']
                    print(item)
            else:
                # 当队列为空时,已经上锁但未释放
                self.lock.release()
                break

    def run(self):
        # 先让URL地址入队列
        self.url_in()
        # 创建多线程运行
        t_list = []
        for i in range(1):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

if __name__ == '__main__':
    start_time = time.time()
    spider = XiaomiSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f' % (end_time - start_time))






