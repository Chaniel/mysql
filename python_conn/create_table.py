# encoding: utf-8
#!/usr/bin/python

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="testuser", passwd="test123",db="testdb" , port=3308, unix_socket='/data/mysql-1/data/mysql.sock')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS employee")

# 创建数据表SQL语句
sql = """CREATE TABLE employee (
         id int NOT NULL AUTO_INCREMENT primary key,
         first_name CHAR(20) NOT NULL,
         last_name  CHAR(20),
         age INT,  
         sex CHAR(1),
         income FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
