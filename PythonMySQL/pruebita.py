import mysql.connector

# Connect to server
config = {
    'user': 'root',
    'password': 'mysqlpass872@',
    'host': 'localhost',
    'database': 'testdb',
    'raise_on_warnings': True
}

# Establish the connection
conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

#cursor.execute("create database testdb")
#cursor.execute("create table students (name varchar(255), age integer)")
cursor.execute("show tables")




print(conexion, " Conexion exitosa")