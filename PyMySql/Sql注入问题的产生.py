"""
Sql注入的产生
"""
import pymysql
connect_db = pymysql.Connect(host="localhost", port=3306,
                             user='root', password='worst123',charset='UTF8', database='jing_dong')
cur = connect_db.cursor()
# 让用户输入数据进行查询
select_id = input('请输入一个查询的id:')

# sql注入问题产生的原因
# 查询时,利用了SQL的合法规则,查询到了不该得到的数据,称为SQL注入
sql_str = ''' select * from goods where id = %s'''% select_id
print(sql_str)
cur.execute(sql_str)
result =cur.fetchall()
print(result)
cur.close()
connect_db.close()