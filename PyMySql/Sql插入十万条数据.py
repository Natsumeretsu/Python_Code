"""
Sql插入十万条数据
"""
import pymysql

connect_db = pymysql.Connect(host="localhost", port=3306,
                             user='root', password='worst123', charset='UTF8', database='jing_dong')

# 开启自动提交
connect_db.autocommit(True)
cur = connect_db.cursor()

sql_str = '''insert into test_index values(%s,%s)'''

# 如果自动提交开启的话,那么需要手动开启事务
# connect_db.begin()

for i in range(10001):
    cur.execute(sql_str, [0, f'data-{i}'])

cur.close()
connect_db.close()
