import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'qwe123',
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS CRM")

print("Database CRM created successfully!")
