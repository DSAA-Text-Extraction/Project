import mysql.connector as mysql #mysql-connector
import sys

db= mysql.connect(user="root",password="your_password",host="localhost",database="dsaa")
mycursor = db.cursor()

"""
 ---- Run dsaa-schema.sql ------
 command : source dsaa-schema.sql
create database if not exists dsaa;
use dsaa;
create table test (id int(10) AUTO_INCREMENT primary key,address varchar(255), UNIQUE(address) );
"""

"""
sql = "INSERT INTO test (address,just) VALUES (%s ,%s)"
val=[('/home/username/dsaa-project/images/OS-1.jpg','1'),('/home/username/dsaa-project/images/OS-2.jpg','1')]
mycursor.executemany(sql,val)
db.commit()
"""
mycursor.execute("select * from test")

data = mycursor.fetchall()

a=[]
for i in data:
	a.append(i[0])
	print i
print a
for i in range(len(a)):
	print i," - ",a[i]
mycursor.close()
db.close()
