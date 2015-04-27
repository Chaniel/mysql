import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="testuser", passwd="test123",db="testdb" , port=3308, unix_socket='/data/mysql-1/data/mysql.sock')

cursor = db.cursor()

cursor.execute("select version()")
data = cursor.fetchone()

print "Database version : %s " % data
db.close()
