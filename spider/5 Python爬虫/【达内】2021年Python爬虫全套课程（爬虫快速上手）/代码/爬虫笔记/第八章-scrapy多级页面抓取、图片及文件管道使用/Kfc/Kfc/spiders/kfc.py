# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import KfcItem

class KfcSpider(scrapy.Spider):
    name = 'kfc'
    allowed_domains = ['www.kfc.com.cn']
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    city_name = input('请输入城市名称：')

    def start_requests(self):
        """重写start_requests()方法,获取某个城市的肯德基门店的总数量"""
        formdata = {
            'cname': self.city_name,
            'pid': '',
            'pageIndex': '1',
            'pageSize': '10',
        }
        yield scrapy.FormRequest(url=self.post_url, formdata=formdata, callback=self.get_total, dont_filter=True)

    def get_total(self, response):
        """获取总页数,并交给调度器入队列"""
        html = json.loads(response.text)
        count = html['Table'][0]['rowcount']
        total_page = count // 10 if count % 10 == 0 else count // 10 + 1
        # 将所有页的URL地址交给调度器入队列
        for page in range(1, total_page + 1):
            formdata = {
                'cname': self.city_name,
                'pid': '',
                'pageIndex': str(page),
                'pageSize': '10',
            }
            # 交给调度器入队列
            yield scrapy.FormRequest(url=self.post_url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        """解析提取具体的门店数据"""
        html = json.loads(response.text)
        for one_shop_dict in html['Table1']:
            item = KfcItem()
            item['rownum'] = one_shop_dict['rownum']
            item['storeName'] = one_shop_dict['storeName']
            item['addressDetail'] = one_shop_dict['addressDetail']
            item['cityName'] = one_shop_dict['cityName']
            item['provinceName'] = one_shop_dict['provinceName']

            # 至此,一个完整的门店数据提取完成,交给项目管道文件处理
            yield item













