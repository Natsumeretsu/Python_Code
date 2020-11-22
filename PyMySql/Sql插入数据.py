"""
通过pymysql插入数据
"""
import pymysql

# 1.创建数据库链接对象,进行链接
connect_db = pymysql.Connect(host="localhost", port=3306,
                             user='root', password='worst123',charset='UTF8', database='jing_dong')

# 2.获取数据库对象的游标对象
cur = connect_db.cursor()

# 3.执行sql语句

sql_str = '''insert into goods(name,cate_id,brand_id) values('MacBookPro 15',1,1);'''

cur.execute(sql_str)
'''
当再对数据库进行增删改的操作时,默认会在事务环境中进行操作,操作完后要进行手动提交操作
,如果不提交,程序默认操作为回滚,那么刚才操作的过程将不会被记录.

事务的提交的操作又数据库连接对象来完成
注意:提交要放在执行后
'''
connect_db.commit()
# 4.关闭游标
cur.close()
# 5.关闭数据库
connect_db.close()