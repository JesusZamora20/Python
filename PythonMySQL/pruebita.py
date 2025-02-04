import mysql.connector

# Connect to server
config = {
    'user': 'root',
    'password': 'mysqlpass872@',
    'host': 'localhost',
    'database': 'sakila',
    'raise_on_warnings': True
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

print(conexion)