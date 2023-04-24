import sqlite3
from sqlite3 import Error
import cv2
import numpy as np
import PIL.Image as Image
import io


def create_connection(db_file):
    """create a database connection to the sqlite database"""
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.close()
    except Error as e:
        print(e)
        
        
def convertToBinaryData(filename):
    image = cv2.imread(filename)
    is_success,im_buf_arr = cv2.imencode(".png",image)
    byte_im = im_buf_arr.tobytes()
    return byte_im

def insertBLOB(empid,name,path,db):
    try:
        sqlite_insert_blob_query = """INSERT INTO new_employee(id,name,photo) VALUES (?,?,?)"""
        empphoto = convertToBinaryData(path)
        data_tuple = (empid,name,empphoto)
        cursor = db.cursor()
        cursor.execute(sqlite_insert_blob_query,data_tuple)
        db.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        return False
    
    
def insert_DB(db_file):
    try:
        sql_create_projects_table= """CREATE TABLE IF NOT EXISTS new_employee(
                            id integer PRIMARY KEY,
                            photo BLOB NOT NULL
                        )"""
        db = create_connection(db_file)
        
        if db is not None:
            create_table(db,sql_create_projects_table)
            
            if(not(insertBLOB(db_file.db))):
                raise Exception("error inserting")
            
            print("\n successfully inserted")
            
        else:
            print("Error! cannot the database connection")
    except sqlite3.Error as error:
        print("\n error while connecting to sqlite", error)
        
        
    finally:
        if(db):
            db.close()
            print("\n db is closed now")
            
if __name__ == '__main__':
    db_file = "db_file.db"
    insert_DB(db_file)
    
