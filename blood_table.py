import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)

cursor = connection.cursor()

cursor.execute("create database if not exists blood_db")
cursor.execute("use blood_db")

cursor.execute("""
create table if not exists donor(
    id int primary key auto_increment,
    name varchar(50),
    blood_group varchar(10),
    phone varchar(15),
    city varchar(50),
    last_donation datetime
)
""")

connection.commit()

print("Database and donor table created successfully")