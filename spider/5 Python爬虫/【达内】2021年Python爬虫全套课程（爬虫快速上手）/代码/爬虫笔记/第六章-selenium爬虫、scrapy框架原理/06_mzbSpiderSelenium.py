"""
使用selenium来抓取民政部网站最新行政区划代码
"""
from selenium import webdriver
import time
import pymysql

class MzbSpider:
    def __init__(self):
        # 设置无界面模式
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/2020/')
        # 创建MySQL相关变量
        self.db = pymysql.connect('localhost', 'root', '123456', 'mzbdb', charset='utf8')
        self.cur = self.db.cursor()

    def parse_html(self):
        self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a').click()
        # 最好给页面加载预留时间
        time.sleep(1)
        # 切换句柄
        li = self.driver.window_handles
        self.driver.switch_to.window(li[1])
        # 提取数据                                                                    
        tr_list = self.driver.find_elements_by_xpath('//table//tr')
        for tr in tr_list[3:]:
            one_city_list = tr.text.split()
            item = {}
            item['name'] = one_city_list[1].strip()
            item['code'] = one_city_list[0].strip()
            print(item)
            ins = 'insert into mzbtab values(%s,%s)'
            self.cur.execute(ins, [item['name'], item['code']])
            self.db.commit()

    def run(self):
        self.parse_html()
        # 断开数据库的链接
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()





















