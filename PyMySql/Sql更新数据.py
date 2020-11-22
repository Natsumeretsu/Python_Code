"""
通过pymysql更新数据
"""
import pymysql

connect_db = pymysql.Connection(host='localhost', port=3306, user='root', password='worst123', charset='UTF8',
                             database='jing_dong')
cur = connect_db.cursor()

# sql_str = '''update goods set cate_id = 8 where id = 24'''
sql_str = '''delete from goods where id = 24'''

cur.execute(sql_str)
connect_db.commit()

cur.close()

connect_db.close()