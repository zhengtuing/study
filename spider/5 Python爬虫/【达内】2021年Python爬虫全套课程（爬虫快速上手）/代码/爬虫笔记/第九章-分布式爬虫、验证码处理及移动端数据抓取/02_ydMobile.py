"""
    F12模拟手机抓包,抓取有道翻译的结果
"""
import requests
from lxml import etree

url = 'http://m.youdao.com/translate'
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
word = input('请输入要翻译的单词:')
data = {
    'inputtext': word,
    'type': 'AUTO',
}
html = requests.post(url=url, data=data, headers=headers).text

p = etree.HTML(html)
result = p.xpath('//ul[@id="translateResult"]/li/text()')[0].strip()
print(result)








