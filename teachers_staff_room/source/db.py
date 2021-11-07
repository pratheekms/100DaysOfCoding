# all database operations are written here
import mysql.connector
import dbconfig


def create_conn(db_name: str) -> mysql.connector:
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
    conn = mysql.connector.connect(host=dbconfig.DATABASE_CONFIG['host'],
                                   user=dbconfig.DATABASE_CONFIG['user'],
                                   password=dbconfig.DATABASE_CONFIG['password'],
                                   db=dbconfig.DATABASE_CONFIG['dbname'])
    return conn


def print_table_data(db_conn: mysql.connector) -> None:
    """[summary]

    Args:
        db_conn (mysql.connector): [description]
    """    
    sql = "select * from teachers"
    mycursor = db_conn.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print('Printing database records:->')
    for x in myresult:
        print(x)


def insert_new_record(db_conn, u_input):
    """[summary]

    Args:
        db_conn ([type]): [description]
        u_input ([type]): [description]
    """    
    sql = "INSERT INTO teachers (first_name, last_name,gender,title,qualification,primary_subject,\
secondary_subject,contact_number,email_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"

    mycursor = db_conn.cursor()
    mycursor.execute(sql, u_input)
    db_conn.commit()
    print(mycursor.rowcount, "record inserted")
    mycursor.execute("select LAST_INSERT_ID()")
    t_id = mycursor.fetchone()
    return t_id[0]


def view_teacher_details(db_conn, teacher_id):
    """[summary]

    Args:
        db_conn ([type]): [description]
        teacher_id ([type]): [description]

    Returns:
        [type]: [description]
    """    
    if validate_teache_id(db_conn, teacher_id):
        t_id = (teacher_id,)
        sql = "select * from teachers where id=%s"

        mycursor = db_conn.cursor()
        mycursor.execute(sql, t_id)

        fields = map(lambda x: x[0], mycursor.description)
        result = [dict(zip(fields, row)) for row in mycursor.fetchall()]
        return result
    else:
        return None


def update_teacher_record(db_conn, col_name, new_val, t_id):
    """[summary]

    Args:
        db_conn ([type]): [description]
        col_name ([type]): [description]
        new_val ([type]): [description]
        t_id ([type]): [description]
    """    
    sql = "UPDATE teachers SET {}=%s WHERE id=%s".format(col_name)
    val = (new_val, t_id,)
    mycursor = db_conn.cursor()
    mycursor.execute(sql, val)
    db_conn.commit()
    print(mycursor.rowcount, "record updated")


def delete_teacher(db_conn, teacher_id):
    """[summary]

    Args:
        db_conn ([type]): [description]
        teacher_id ([type]): [description]
    """    
    sql = "DELETE FROM teachers WHERE id=%s"
    val = (teacher_id,)
    mycursor = db_conn.cursor()
    mycursor.execute(sql, val)
    db_conn.commit()
    print(mycursor.rowcount, "record deleted")


def validate_teache_id(db_conn, teacher_id):
    """[summary]

    Args:
        db_conn ([type]): [description]
        teacher_id ([type]): [description]

    Returns:
        [type]: [description]
    """    
    t_id = (teacher_id,)
    sql = "select id from teachers where id=%s"
    mycursor = db_conn.cursor()
    mycursor.execute(sql, t_id)
    record = mycursor.fetchone()
    row_count = mycursor.rowcount
    if row_count == 0:
        return False
    else:
        return True


def get_column_names(db_conn):
    """[summary]

    Args:
        db_conn ([type]): [description]

    Returns:
        [type]: [description]
    """    
    sql = "select * from teachers"

    mycursor = db_conn.cursor()
    mycursor.execute(sql)

    col_names = list(map(lambda x: x[0], mycursor.description))
    mycursor.reset()
    return col_names
