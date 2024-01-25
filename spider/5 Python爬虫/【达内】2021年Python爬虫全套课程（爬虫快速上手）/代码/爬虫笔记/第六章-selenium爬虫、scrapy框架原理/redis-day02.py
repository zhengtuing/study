# """
# 目标：查看用户信息,先到redis中查询,如果未缓存则到mysql中查询
# 说明：redis中,用户名作为key,不同维度用户信息作为field及value
# 思路：
#     1、接收用户从终端输入查询用户名
#     2、到redis中查询
#     3、redis中未查到,则到MySQL中查询,然后缓存到redis中一份,并设置过期时间
# 前提-MySQL建库建表,并存储相关用户信息：
# mysql -uroot -p123456
# create database userdb charset utf8;
# use userdb;
# create table user_tab(
# id int primary key auto_increment,
# username varchar(30),
# age tinyint,
# gender char(1)
# )charset=utf8;
# insert into user_tab(username,age,gender) values('DaNiu',30,'F');
# """
# import redis
# import pymysql
#
# r = redis.Redis(host='localhost', port=6379, db=0)
# db = pymysql.connect('localhost', 'root', '123456', 'userdb', charset='utf8')
# cur = db.cursor()
#
# # 1、接收用户输入查询用户名
# name = input('请输入查询用户名:')
# # 2、到redis中查询(user_info_dict可能为空字典,或者非空字典)
# user_info_dict = r.hgetall(name)
# if user_info_dict:
#     print('redis result:', user_info_dict)
# else:
#     sel = 'select age,gender from user_tab where username=%s'
#     cur.execute(sel, [name])
#     user_info_tuple = cur.fetchall()
#     print('mysql result:', user_info_tuple)
#     # 将数据缓存到redis中,并设置过期时间
#     r.hmset(name, {'age':user_info_tuple[0][0], 'gender':user_info_tuple[0][1]})
#     r.expire(name, 20)
#
#
# # 结果分析:
# # 1、第一次查询,redis中未缓存,所以结果为mysql中
# # 2、30秒内进行第二次查询,redis中已缓存,所以结果为redis中
# # 3、30秒之后,redis中缓存消失,所以结果为mysql中


# """
# 代码二：用户修改个人信息时，要将数据同步到redis缓存
# 目标及思路：
#     1、用户修改个人信息
#     2、先到MySQL数据库中修改
#     3、再缓存到redis中,或者将redis中原来缓存的更新
# """
# import redis
# import pymysql
#
# class Update:
#     def __init__(self):
#         self.r = redis.Redis(host='localhost', port=6379, db=0)
#         self.db = pymysql.connect('localhost', 'root', '123456', 'userdb', charset='utf8')
#         self.cur = self.db.cursor()
#
#     def update_mysql(self, age, username):
#         """更新MySQL表记录函数"""
#         upd = 'update user_tab set age=%s where username=%s'
#         self.cur.execute(upd, [age, username])
#         self.db.commit()
#         print('修改成功')
#
#     def update_redis(self, username, age):
#         """同步到redis数据库函数"""
#         user_info_dict = self.r.hgetall(username)
#         # 之前已经缓存,则更新age,否则重新缓存
#         if user_info_dict:
#             self.r.hset(username, 'age', age)
#         else:
#             # 到mysql中查询此用户最新信息缓存到redis
#             self.mysql_to_redis(username)
#
#     def mysql_to_redis(self, username):
#         sel = 'select age,gender from user_tab where username=%s'
#         self.cur.execute(sel, [username])
#         user_info_tuple = self.cur.fetchall()
#         # 缓存到redis并设置缓存时间
#         user_dict = {'age':user_info_tuple[0][0], 'gender':user_info_tuple[0][1]}
#         self.r.hmset(username, user_dict)
#         self.r.expire(username, 30)
#
#     def main(self):
#         username = input('请输入用户名:')
#         age = input('请输入新成绩:')
#         self.update_mysql(username, age)
#         self.update_redis(username, age)
#
# if __name__ == '__main__':
#     up = Update()
#     up.main()

# import requests
# from threading import Thread,Lock
# from queue import Queue
# from fake_useragent import UserAgent
# import os
# from urllib import parse
# import time
#
# class BaiduImageSpider:
#     def __init__(self):
#         self.keyword = input('请输入关键字:')
#         self.directory = './images/{}/'.format(self.keyword)
#         if not os.path.exists(self.directory):
#             os.makedirs(self.directory)
#         # 编码
#         self.params = parse.quote(self.keyword)
#         self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&hd=&latest=&copyright=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={}&rn=30&gsm=5a&1599724879800='
#         # 创建url队列、线程锁
#         self.url_queue = Queue()
#         self.lock = Lock()
#
#     def get_html(self, url):
#         """请求功能函数"""
#         headers = {'User-Agent' : UserAgent().random}
#         html = requests.get(url=url, headers=headers).json()
#
#         return html
#
#     def get_total_image(self):
#         """获取图片总数量"""
#         total_page_url = self.url.format(self.params, self.params, 0)
#         total_page_html = self.get_html(url=total_page_url)
#         total_page_nums = total_page_html['displayNum']
#
#         return total_page_nums
#
#     def url_in(self):
#         total_image_nums = self.get_total_image()
#         for pn in range(0, total_image_nums, 30):
#             page_url = self.url.format(self.params, self.params, pn)
#             self.url_queue.put(page_url)
#
#     def parse_html(self):
#         """线程事件函数"""
#         while True:
#             # 加锁
#             self.lock.acquire()
#             if not self.url_queue.empty():
#                 page_url = self.url_queue.get()
#                 # 释放锁
#                 self.lock.release()
#                 html = self.get_html(url=page_url)
#                 for one_image_dict in html['data']:
#                     try:
#                         image_url = one_image_dict['hoverURL']
#                         self.save_image(image_url)
#                     except Exception as e:
#                         continue
#             else:
#                 self.lock.release()
#                 break
#
#     def save_image(self, image_url):
#         """保存一张图片到本地"""
#         headers = {'User-Agent':UserAgent().random}
#         image_html = requests.get(url=image_url, headers=headers).content
#         # 加锁、释放锁
#         self.lock.acquire()
#         filename = self.directory + image_url[-24:]
#         self.lock.release()
#         with open(filename, 'wb') as f:
#             f.write(image_html)
#         print(filename, '下载成功')
#
#     def run(self):
#         # 让URL地址入队列
#         self.url_in()
#         # 创建多线程
#         t_list = []
#         for i in range(1):
#             t = Thread(target=self.parse_html)
#             t_list.append(t)
#             t.start()
#
#         for t in t_list:
#             t.join()
#
# if __name__ == '__main__':
#     start_time = time.time()
#     spider = BaiduImageSpider()
#     spider.run()
#     end_time = time.time()
#     print('time:%.2f' % (end_time - start_time))


import requests
def geocode(address):
    parameters = {'address': address, 'key': '389fa04d8f91a2416b9f7b23bdaf7d1e'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    if answer['count'] == '0':
        return "error", "", "", ""
    dz = answer['geocodes'][0]['formatted_address']
    qu = answer['geocodes'][0]['city'] + answer['geocodes'][0]['district']
    adcode = answer['geocodes'][0]['adcode']
    location = answer['geocodes'][0]['location']
    return location

print(geocode('天安门'))










