"""
Sql注入的解决
"""
import pymysql

connect_db = pymysql.Connect(host="localhost", port=3306,
                             user='root', password='worst123', charset='UTF8', database='jing_dong')
cur = connect_db.cursor()
# 让用户输入数据进行查询
select_id = input('请输入一个查询的id:')

# sql注入问题产生的原因
# 查询时,利用了SQL的合法规则,查询到了不该得到的数据,称为SQL注入
sql_str = ''' select * from goods where id = %s'''
print(sql_str)
# 利用execute方法的第二个参数,了解决SQL注入的问题,利用参数化来解决SQL注入
cur.execute(sql_str, (select_id,))
result = cur.fetchall()
print(result)
cur.close()
connect_db.close()
