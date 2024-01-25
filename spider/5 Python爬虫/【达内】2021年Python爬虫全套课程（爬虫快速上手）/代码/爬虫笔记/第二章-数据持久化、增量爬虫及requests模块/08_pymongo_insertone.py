"""
在 maoyandb 库的 maoyanset 集合中, 插入1条文档
"""
import pymongo

# 1、连接对象
conn = pymongo.MongoClient(host='localhost', port=27017)
# 2、库对象
db = conn['maoyandb']
# 3、集合对象
myset = db['maoyanset']
# 4、插入文档 - 一次插入1条文档
myset.insert_one({'name':'泰坦尼克号','star':'T','time':'1990-01-01'})

# 5、插入文档 - 一次性插入多条文档 [{},{},{}]
film_li = [
    {'name':'风之子','star':'Tom','time':'1991-01-01'},
    {'name':'雄霸天下','star':'Dong','time':'1992-01-01'}
]
myset.insert_many(film_li)











