"""
使用params参数向贴吧发请求
注意：
    1、URL地址为基准的URL地址,不包含查询参数
    2、params中的键值对为所有的查询参数
"""
import requests

url = 'http://tieba.baidu.com/f?'
params = {'kw':'迪丽热巴吧', 'pn':'50'}
headers = {'User-Agent' : 'Mozilla/5.0'}
# 开始请求
html = requests.get(url=url, params=params, headers=headers).text
print(html)




