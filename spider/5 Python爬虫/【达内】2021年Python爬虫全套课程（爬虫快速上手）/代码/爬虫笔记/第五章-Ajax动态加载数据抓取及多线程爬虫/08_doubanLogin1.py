"""
利用Cookie模拟登录豆瓣网
"""
import requests

def login():
    url = 'https://www.douban.com/people/211922653/'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Cookie':'ll="118097"; bid=Mb0t8WRINYY; _pk_ses.100001.8cb4=*; dbcl2="211922653:CFixXQMv1bU"; ck=Ihko; ap_v=0,6.0; __yadk_uid=C4YsGfVQfDEG3LrHpY7qMd91qdvqtCYK; douban-profile-remind=1; _pk_id.100001.8cb4=5e91e219362a83c1.1598409888.1.1598409913.1598409888.; push_noty_num=0; push_doumail_num=0; __utma=30149280.715367562.1598409918.1598409918.1598409918.1; __utmc=30149280; __utmz=30149280.1598409918.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=30149280.21192; __utmb=30149280.2.10.1598409918'
    }
    html = requests.get(url=url, headers=headers).text
    # 确认html中是否存在我账号的信息：永远
    print(html)

login()










