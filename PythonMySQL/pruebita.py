import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="mysqlpass872@",
    database="sakila"
)

print(mydb)

