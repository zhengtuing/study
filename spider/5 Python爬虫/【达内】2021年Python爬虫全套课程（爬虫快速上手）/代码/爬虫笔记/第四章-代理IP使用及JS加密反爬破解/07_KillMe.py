"""
让西刺代理IP网站干掉我！
"""

import requests

url = 'https://www.xicidaili.com/nn/{}'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
proxies = {
    'http' : 'http://309435365:szayclhp@116.255.166.47:16819',
    'https' : 'https://309435365:szayclhp@116.255.166.47:16819',
}

for i in range(1,2):
    print(i)
    url = url.format(i)
    html = requests.get(url=url, proxies=proxies, headers=headers).text
    print(html)