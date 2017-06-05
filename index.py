import _mysql
import sys

try:
	con = _mysql.connect('localhost', 'root', '', 'db_py')
	con.query("SELECT VERSION()")

	print "Mysql version: %s" % \
	result.fetch_row()[0]

except Exception as e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

finally:
	if con:
		con.close()


# import MySQLdb

# # Open database connection
# db = MySQLdb.connect(“localhost”,”siddhu”,”siddhu”,”testsiddhu” )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # execute SQL query 
# cursor.execute(“SELECT VERSION()”)

# # Fetch a single row 
# data = cursor.fetchone()

# print (“Database version : %s ” % data)

# # Drop table if it already exist 
# cursor.execute(“DROP TABLE IF EXISTS SIDDHU_TEST”)

# # Create table Example
# sql = “””CREATE TABLE SIDDHU_TEST (
# FNAME CHAR(20) NOT NULL,
# LNAME CHAR(20),
# AGE INT, 
# GENDER CHAR(1),
# INCOME FLOAT )”””

# cursor.execute(sql)
