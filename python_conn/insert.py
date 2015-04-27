# encoding: utf-8
#!/usr/bin/python

import MySQLdb
from random import Random

def random_str(randomlength=5):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="testuser", passwd="test123",db="testdb" , port=3308, unix_socket='/data/mysql-1/data/mysql.sock')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()


for i in xrange(1,500000):

    # SQL 插入语句
    # method 1
    #sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    #         LAST_NAME, AGE, SEX, INCOME)
    #         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    
    # method 2
    sql = "INSERT INTO employee(first_name, last_name, age, sex, income) \
           VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
           (random_str(), 'Mohan', 20, 'M', 2000)
    
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except Exception,e:
       # Rollback in case there is any error
       db.rollback()

# 关闭数据库连接
db.close()
