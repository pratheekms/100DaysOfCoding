import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='pmsadmin',
                               password='pmspratheek1',
                               database='teachersstaffroom')

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE teachersstaffroom")

# mycursor.execute(
#     "CREATE TABLE teachers (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255),\
#         last_name VARCHAR(255),\
#      gender VARCHAR(7),title VARCHAR(130),qualification VARCHAR(10),\
#          primary_subject VARCHAR(20),secondary_subject VARCHAR(30),\
#          contact_number VARCHAR(10),email_id VARCHAR(25))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

sql="INSERT INTO teachers (first_name, last_name,gender,title,qualification,primary_subject,\
secondary_subject,contact_number,email_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
val=('shivkumar','K C','M','Head Master','B.Ed','Kannada','Social Science','123456789','kcshikumar@school.com')
mycursor.execute(sql,val)
mydb.commit()




# db = mysql.connector.connect(host='localhost',
#                              user='pmsadmin',
#                              password='pmspratheek1',
#                              database='teachersstaffroom')
# mycursor = db.cursor()
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)