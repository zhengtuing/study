"""
excutemany()方法,一次性插入多条表记录,提升数据库的效率
"""
import pymysql

db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
cursor = db.cursor()

ins = 'insert into maoyantab values(%s,%s,%s)'
film_li = [
    ('喜剧之王','周星驰','1994-01-01'),
    ('唐伯虎点秋香','周星驰','1995-01-01')
]
cursor.executemany(ins,film_li)

db.commit()
cursor.close()
db.close()





