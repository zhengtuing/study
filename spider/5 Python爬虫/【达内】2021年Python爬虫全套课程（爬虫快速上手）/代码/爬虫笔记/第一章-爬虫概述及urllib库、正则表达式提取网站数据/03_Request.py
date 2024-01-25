"""
使用Request()方法包装请求,并使用测试网站来验证
"""
from urllib import request

# 1、定义常用变量
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
# 2、包装请求
req = request.Request(url=url,headers=headers)
# 3、发请求
res = request.urlopen(req)
# 4、获取响应内容
html = res.read().decode()
print(html)






