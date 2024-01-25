"""
在maoyandb库的maoyantab表中插入1条表记录
"""
import pymysql

# 1、创建数据库连接对象 + 游标对象
db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
cursor = db.cursor()
# 2、利用游标对象的 execute() 方法执行SQL命令
ins = 'insert into maoyantab values(%s,%s,%s)'
cursor.execute(ins,['大话西游之月光宝盒','周星驰','1993-01-01'])
# 3、提交到数据库执行：commit()
db.commit()
# 4、关闭游标 + 断开数据库连接
cursor.close()
db.close()









