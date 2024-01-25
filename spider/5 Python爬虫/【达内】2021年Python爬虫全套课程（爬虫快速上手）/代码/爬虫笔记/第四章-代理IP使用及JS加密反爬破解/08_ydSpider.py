"""
有道翻译,翻译结果抓取
"""
import requests
import time
import random
from hashlib import md5

class YdSpider:
    def __init__(self):
        # post_url: 浏览器F12抓到的POST的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # Cookie Referer User-Agent 是网站反爬检查频率比较高的3个字段
            "Cookie": "OUTFOX_SEARCH_USER_ID=197778081@10.108.160.105; OUTFOX_SEARCH_USER_ID_NCOO=350557135.77273035; JSESSIONID=aaaqHiKiNEm72aeLkN7fx; ___rl__test__cookies=1586921985497",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        }

    def md5_string(self, string):
        """功能函数：对字符串进行md5的加密"""
        s = md5()
        s.update(string.encode())

        return s.hexdigest()

    def get_ts_salt_sign(self, word):
        """获取 ts salt sign"""
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        sign = self.md5_string(string)

        return ts, salt, sign

    def attack_yd(self, word):
        # 获取ts、salt、sign
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "46dc72e3f78c8e58e69300149bb03d64",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # 注意：此处一定要使用 post 方法
        # .json() ：作用是把一个json格式的字符串 转为 Python数据类型
        html = requests.post(url=self.post_url, data=data, headers=self.headers).json()

        return html['translateResult'][0][0]['tgt']

    def run(self):
        word = input('请输入要翻译的单词:')
        result = self.attack_yd(word)
        print(result)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()












