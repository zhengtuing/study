"""
使用 独享|私密 代理IP访问测试网站并确认IP
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent' : 'Mozilla/5.0'}
proxies = {
    'http' : 'http://309435365:szayclhp@116.255.166.47:16819',
    'https' : 'https://309435365:szayclhp@116.255.166.47:16819',
}

html = requests.get(url=url, proxies=proxies, headers=headers).text
print(html)