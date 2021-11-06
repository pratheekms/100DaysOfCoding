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


# create table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# print(x for x in mycursor.execute("SHOW TABLES"))
# sql="DROP TABLE customrs"
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# sql="ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"

sql='INSERT INTO customers (name,address) VALUES ( %s,%s)'
val=('cena','india')
mycursor.execute(sql,val)
db.commit()
print(mycursor.rowcount,"record inserted")

# excetuce many, for multiple insert
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# db.commit()

# print(mycursor.rowcount, "was inserted.") 

# sql="select * from customers"
sql="select LAST_INSERT_ID()"
mycursor.execute(sql)
tid=mycursor.fetchone()
print(tid)

# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# # myresult=mycursor.fetchone()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers WHERE name =%s"
# # adr = ("Yellow Garden 2", )
# name=("john",)

# mycursor.execute(sql,name)

# res=mycursor.fetchall()
# for x in res:
#     print(x)

# sql_update="UPDATE customers SET NAME=%s WHERE NAME=%s"
# name=('john','JOHN')
# mycursor.execute(sql_update,name)
# db.commit()
