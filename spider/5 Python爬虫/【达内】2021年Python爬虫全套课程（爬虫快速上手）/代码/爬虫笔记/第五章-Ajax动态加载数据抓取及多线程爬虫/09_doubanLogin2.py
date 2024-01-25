"""
利用Cookie进行模拟登录豆瓣网 - 利用cookies参数
思路:
    1、先登录成功一次,F12抓到登录成功的Cookie
    2、把字符串格式的Cookie处理为 字典,作为requests.get()方法中的cookies参数的值
"""
import requests

def login2():
    url = 'https://www.douban.com/people/211922653/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    cookies = get_cookies()
    html = requests.get(url=url, headers=headers, cookies=cookies).text
    # 测试: html中是否存在账号相关的内容(永远的账号)
    print(html)

def get_cookies():
    """功能: 处理字符串形式的Cookie为字典类型"""
    cookies = {}
    cookies_string = 'll="118097"; bid=Mb0t8WRINYY; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __yadk_uid=C4YsGfVQfDEG3LrHpY7qMd91qdvqtCYK; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; __utma=30149280.715367562.1598409918.1598409918.1598409918.1; __utmc=30149280; __utmz=30149280.1598409918.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.21192; __utmb=30149280.5.10.1598409918; dbcl2="211922653:x8G6gh89gSg"; ck=6K5X; _pk_id.100001.8cb4=5e91e219362a83c1.1598409888.1.1598411081.1598409888.'
    for kv in cookies_string.split('; '):
        key = kv.split('=')[0]
        value = kv.split('=')[1]
        cookies[key] = value

    # 此循环结束后,cookies为最终的字典
    return cookies

login2()



























