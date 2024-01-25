"""
抓取指定贴吧的所有帖子中的图片
"""
import requests
from lxml import etree
import time
import random
from urllib import parse

class TiebaImageSpider:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        # 此处适用IE的User-Agent
        self.headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'}

    def get_html(self, url):
        """功能函数1 - 请求"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def xpath_func(self, html, xpath_bds):
        """功能函数2 - 解析"""
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)

        return r_list

    def parse_html(self, one_url):
        """一级页面: 提取帖子链接,依次向每个帖子链接发请求,最终下载图片"""
        one_html = self.get_html(url=one_url)
        one_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        href_list = self.xpath_func(html=one_html,xpath_bds=one_xpath)
        for href in href_list:
            # 拿到1个帖子的链接,把这个帖子中所有的图片保存到本地
            self.get_image(href)

    def get_image(self, href):
        """功能：把1个帖子中所有的图片保存到本地"""
        two_url = 'http://tieba.baidu.com' + href
        two_html = self.get_html(url=two_url)
        two_xpath = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        # img_list: ['图片1链接','图片2链接',...]
        img_list = self.xpath_func(html=two_html, xpath_bds=two_xpath)
        for img in img_list:
            html = requests.get(url=img, headers=self.headers).content
            filename = img[-10:]
            with open(filename, 'wb') as f:
                f.write(html)
            print(filename,'下载成功')
            time.sleep(random.randint(0,1))

    def run(self):
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        name = parse.quote(name)
        for i in range(start, end+1):
            pn = (i-1)*50
            one_url = self.url.format(name, pn)
            self.parse_html(one_url)

if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.run()


