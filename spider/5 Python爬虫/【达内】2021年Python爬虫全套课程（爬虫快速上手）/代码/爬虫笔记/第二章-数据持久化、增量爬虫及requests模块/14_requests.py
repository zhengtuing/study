"""
requests模块示例
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'xxxxxxxxxxxxxxxxxxxxx'}

# 写法1
res = requests.get(url=url,headers=headers)
# 获取响应内容
html = res.text

# 写法2
html = requests.get(url=url,headers=headers).text
print(html)




