"""
把赵丽颖的图片,抓取下来,保存到本地
"""
import requests
import os

image_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1584357180699&di=615adaae1a9e068d6ac15544cec16b2b&imgtype=0&src=http%3A%2F%2Feducation.news.cn%2F2015-07%2F29%2F128067978_14380678156761n.jpg'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# 1、content属性：获取bytes数据类型
html = requests.get(url=image_url,headers=headers).content

# 2、确定图片保存路径
directory = './images/'
if not os.path.exists(directory):
    os.makedirs(directory)

# 3、保存到本地文件,filename: ./images/xxxx.jpg
filename = directory + image_url[-10:]
with open(filename,'wb') as f:
    f.write(html)




