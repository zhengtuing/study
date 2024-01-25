"""
Cookie模拟登录豆瓣网-第三种方式（利用requests模块的session对象）
思路:
    1、登录页输入错误的密码抓包,抓到向服务器的哪个地址发送了哪些数据进行的验证
    2、模拟浏览器利用session对象发送请求先验证登录
    3、一旦登录成功,肆意地去抓取任何需要登录才能访问地页面
"""
import requests

s = requests.session()

def login3():
    # post_url: F12抓包抓到的,验证登录的地址
    post_url = 'https://accounts.douban.com/j/mobile/login/basic'
    get_url = 'https://www.douban.com/people/211922653/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Cookie':'ll="118097"; bid=Mb0t8WRINYY; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __yadk_uid=C4YsGfVQfDEG3LrHpY7qMd91qdvqtCYK; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; __utma=30149280.715367562.1598409918.1598409918.1598409918.1; __utmc=30149280; __utmz=30149280.1598409918.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.21192; __utmb=30149280.12.10.1598409918; dbcl2="211922653:yQt98vfGcv4"; ck=oo6c; _pk_id.100001.8cb4=5e91e219362a83c1.1598409888.1.1598413003.1598409888.'
    }
    form_data = {
        'ck':'',
        'name': '15110225726',
        'password': 'zhanshen001',
        'remember': 'false',
        'ticket' : '',
    }
    # 1、先登录
    s.post(url=post_url, headers=headers, data=form_data).text
    # 2、再抓取新页面
    html = s.get(url=get_url, headers=headers).text
    # 在响应内容中确认是否有账号相关信息(永远的账号)
    print(html)

login3()




















