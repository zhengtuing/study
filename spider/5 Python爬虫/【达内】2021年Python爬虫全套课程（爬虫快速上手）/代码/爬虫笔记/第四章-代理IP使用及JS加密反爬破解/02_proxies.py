"""
使用免费代理IP访问测试网站并确认IP
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent' : 'Mozilla/5.0'}
proxies = {
    'http' : 'http://182.92.113.148:8118',
    'https' : 'https://182.92.113.148:8118',
}

html = requests.get(url=url, proxies=proxies, headers=headers).text
print(html)

