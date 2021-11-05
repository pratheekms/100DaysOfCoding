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
