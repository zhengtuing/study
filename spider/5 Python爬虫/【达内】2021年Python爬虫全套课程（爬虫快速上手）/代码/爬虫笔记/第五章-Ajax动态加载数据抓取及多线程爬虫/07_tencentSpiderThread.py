"""
多线程抓取腾讯招聘职位的信息
"""
import requests
from threading import Thread,Lock
from queue import Queue
import time
from urllib import parse
from fake_useragent import UserAgent

class TencentSpider:
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582659&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1587188248553&postId={}&language=zh-cn'
        # 2个队列
        self.one_q = Queue()
        self.two_q = Queue()
        # 2把锁
        self.lock1 = Lock()
        self.lock2 = Lock()
        # 计数
        self.number = 0

    def get_html(self, url):
        """功能函数1：获取响应内容"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).json()

        return html

    def url_in(self):
        """一级页面的URL地址入队列"""
        keyword = input('请输入职位类别：')
        keyword = parse.quote(keyword)
        # 获取总页数
        total = self.get_total(keyword)
        for page in range(1,total+1):
            url = self.one_url.format(keyword, page)
            self.one_q.put(url)

    def get_total(self, keyword):
        """获取某个类别的总页数"""
        url = self.one_url.format(keyword, 1)
        html = self.get_html(url=url)
        count = html['Data']['Count']
        total = count//10 if count%10==0 else count//10 + 1

        return total

    def parse_one_page(self):
        """一级页面解析函数：提取postid,并拼接二级页面URL地址,入队列"""
        while True:
            # 上锁
            self.lock1.acquire()
            if not self.one_q.empty():
                one_url = self.one_q.get()
                # 释放锁
                self.lock1.release()
                one_html = self.get_html(url=one_url)
                # one_html中会有10个postid
                for one_job in one_html['Data']['Posts']:
                    post_id = one_job['PostId']
                    job_url = self.two_url.format(post_id)
                    # 将职位详情页链接交给二级队列
                    self.two_q.put(job_url)
            else:
                self.lock1.release()
                break

    def parse_two_page(self):
        """二级页面解析函数：提取具体的职位信息"""
        while True:
            try:
                self.lock2.acquire()
                two_url = self.two_q.get(timeout=1)
                self.lock2.release()
                two_html = self.get_html(url=two_url)
                item = {}
                item['name'] = two_html['Data']['RecruitPostName']
                item['type'] = two_html['Data']['CategoryName']
                item['address'] = two_html['Data']['LocationName']
                item['duty'] = two_html['Data']['Responsibility']
                item['require'] = two_html['Data']['Requirement']
                item['time'] = two_html['Data']['LastUpdateTime']
                print(item)

                self.lock2.acquire()
                self.number += 1
                self.lock2.release()

            except Exception as e:
                self.lock2.release()
                break

    def run(self):
        """程序入口函数"""
        self.url_in()
        # 创建多线程
        t1_list = []
        t2_list = []
        for i in range(1):
            t1 = Thread(target=self.parse_one_page)
            t1_list.append(t1)
            t1.start()

        for i in range(1):
            t2 = Thread(target=self.parse_two_page)
            t2_list.append(t2)
            t2.start()

        for t1 in t1_list:
            t1.join()

        for t2 in t2_list:
            t2.join()

        print('number:',self.number)

if __name__ == '__main__':
    start_time = time.time()
    spider = TencentSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f' % (end_time - start_time))








