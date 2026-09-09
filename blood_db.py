import mysql.connector
from pymsgbox import password

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)

mycursor = mydb.cursor()
# mycursor.execute("create database blood_db")
# print("Database created successfully...!")

mycursor.execute("SHOW DATABASES")
print(mycursor.fetchall())