# all database operations are written here
import mysql.connector
import dbconfig



def create_conn(db_name:str)->mysql.connector:
    if db_name != dbconfig.DATABASE_CONFIG['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    conn=mysql.connector.connect(host=dbconfig.DATABASE_CONFIG['host'],
                           user=dbconfig.DATABASE_CONFIG['user'],
                           password=dbconfig.DATABASE_CONFIG['password'],
                           db=dbconfig.DATABASE_CONFIG['dbname'])