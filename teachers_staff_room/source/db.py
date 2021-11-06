# all database operations are written here
import mysql.connector
import dbconfig



def create_conn(db_name:str)->mysql.connector:
    """[summary]

    Args:
        db_name (str): [description]

    Raises:
        ValueError: [description]

    Returns:
        mysql.connector: [description]
    """    
    if db_name != dbconfig.DATABASE_CONFIG['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    conn=mysql.connector.connect(host=dbconfig.DATABASE_CONFIG['host'],
                           user=dbconfig.DATABASE_CONFIG['user'],
                           password=dbconfig.DATABASE_CONFIG['password'],
                           db=dbconfig.DATABASE_CONFIG['dbname'])
    return conn

def print_table_data(db_conn:mysql.connector)->None:
    sql="select * from teachers"
    mycursor=db_conn.cursor()
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    print('Printing database records:->')
    for x in myresult:
        print(x)


def insert_new_record(db_conn, u_input):
    sql = "INSERT INTO teachers (first_name, last_name,gender,title,qualification,primary_subject,\
secondary_subject,contact_number,email_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"

    mycursor = db_conn.cursor()
    mycursor.execute(sql, u_input)
    db_conn.commit()
    print(mycursor.rowcount,"record inserted")
    mycursor.execute("select LAST_INSERT_ID()")
    t_id=mycursor.fetchone()
    print('teacher id is:',t_id[0])
    return t_id[0]


def view_teacher_details(db_conn,teacher_id):
    if validate_teache_id(db_conn,teacher_id):
        t_id=(teacher_id,)
        sql="select * from teachers where id=%s"
        
        mycursor=db_conn.cursor()
        mycursor.execute(sql,t_id)
    
        fields = map(lambda x:x[0], mycursor.description)
        result = [dict(zip(fields,row)) for row in mycursor.fetchall()]
        return result
    else:
        return None





def validate_teache_id(db_conn,teacher_id):
    t_id=(teacher_id,)
    sql="select id from teachers where id=%s"
    mycursor=db_conn.cursor()
    mycursor.execute(sql,t_id)
    record=mycursor.fetchone()
    row_count=mycursor.rowcount
    if row_count==0:
        return False
    else:
        return True



