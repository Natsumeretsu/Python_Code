"""
通过pymysql模块在程序中操作数据库
"""
import pymysql

# 1.创建数据库链接对象
# 链接数据库时,除了端口参数外,其余参数都要使用字符串类型
connect_db = pymysql.connect(host='localhost', port=3306, user="root",
                             password="worst123", charset="utf8", database="jing_dong")

# 2.获取游标对象
cur = connect_db.cursor()

# 3.编写数据库操作指令并执行
# 3.1 写数据库操作指令
# sql_str = '''select * from goods where name = "超极本";'''
sql_str = '''select * from goods;'''

# 3.2执行sql语句 cur.execute返回Number of affected rows受到影响的行数
row_count = cur.execute(sql_str)
print(f"查询到{row_count}条记录")

# 3.3 获取一条查询结果
result = cur.fetchone()
print(result)
print("*"*30)
# 3.4 获取指定条数据的记录
result = cur.fetchmany(4)
for t in result:
    print(t)
print("*" * 30)

# 3.5 获取所有数据
result = cur.fetchall()
for t in result:
    print(t)
print("*" * 30)
# 4.关闭游标对象
cur.close()

# 5.关闭数据库对象
connect_db.close()