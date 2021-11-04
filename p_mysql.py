# database mysql

import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='pmsadmin',
                               password='pmspratheek1')

print(mydb)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE pytestdb")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

print('-'*15)
print('-'*15)
# create a new connection
db = mysql.connector.connect(host='localhost',
                             user='pmsadmin',
                             password='pmspratheek1',
                             database='pytestdb')

print(db)

mycursor = db.cursor()
# mycursor.execute('show databases')


#create table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# print(x for x in mycursor.execute("SHOW TABLES"))
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)