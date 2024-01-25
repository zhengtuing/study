"""
urlencode()示例：百度搜索关键字,保存 关键字.html 到本地html文件
"""
from urllib import request
from urllib import parse

# 1、拼接URL地址
word = input('请输入百度搜索关键字:')
params = parse.urlencode({'wd':word})
url = 'http://www.baidu.com/s?{}'.format(params)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# 2、发请求获取响应内容
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode()

# 3、保存到本地文件
filename = word + '.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)














