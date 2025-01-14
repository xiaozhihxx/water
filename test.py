# pymysql用connect方法进行连接
import pymysql

conn = pymysql.connect(host='101.200.234.142', port=3306,
                       user='root', password='abcd19890120',
                       database='demo', charset='utf8mb4')

def con_my_sql(sql_code, params=None):
    try:
        conn.ping(reconnect=True) # 保证数据库连接正常
        print(sql_code)
        # 通过游标对象对数据库服务器发出sql语句
        cursor = conn.cursor(pymysql.cursors.DictCursor) # 返回数据是字典形式，而不是数组
        cursor.execute(sql_code, params or ())
        # 提交
        conn.commit()

        # 获取受影响的行数
        # affected_rows = cursor.rowcount
        # 关闭游标
        #vcursor.close()
        return cursor # affected_rows # 返回受影响的行数
    except pymysql.MySQLError as err_message:
        # 回滚
        conn.rollback()
        # 关闭链接
        conn.close()
        return type(err_message), err_message

# add：使用参数化查询插入数据
# username = 'hxx'
# pwd = '123456'
# code = 'INSERT INTO users (username, password) VALUES (%s, %s)'
# result = con_my_sql(code, (username, pwd))

# query
# username = 'xiaozhi'
# pwd = '123456'
# code = 'select * from users'
# result = con_my_sql(code)

# 打印结果
# print(result.fetchall())

# 关闭数据库连接（如果在其他地方不再使用）
#conn.close()

