"""
向百度发起请求,并获取百度的响应内容
"""
from urllib import request

res = request.urlopen(url='http://www.baidu.com/')
# 响应对象方法1：read() -> bytes
html = res.read().decode()
# 响应对象方法2：geturl() -> 返回实际数据的URL地址
url = res.geturl()
# 响应对象方法3：getcode() -> 返回HTTP响应码
code = res.getcode()






