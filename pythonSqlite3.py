import sqlite3
from sqlite3 import Error
import cv2
import numpy as np
import PIL.Image as Image
import io


def create_connection(db_file):
    """ create a database connection to the sqlite database"""

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.close()
    except Error as e:
        print(e)



def convertToBinaryData(filename): # this uses opencv functions to read image , imencode to encode to a png format and then to bytes
    image = cv2.imread(filename)
    is_success,im_buf_arr = cv2.imencode(".png",image)
    byte_im = im_buf_arr.tobytes()
    return byte_im





def insertBLOB(empid,name,path,db):
    try:
        sqlite_insert_blob_query = """INSERT INTO new_employee (id,name,photo) VALUES (?,?,?) """
        empphoto = convertToBinaryData(path) #convert to binary data
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
        #create a query here, if table does not exist create it or if exist go to next step
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS new_employee(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        photo BLOB NOT NULL
                                    )"""
        #create a database connection
        db = create_connection(db_file)

        #create tables and insert images and data
        if db is not None:
            create_table(db,sql_create_projects_table)

            if(not (insertBLOB(1,'manoj','G:\inputs\Image_Databases\standard\coins.png',db))):
               raise Exception("error inserting")
            
            print("\n successfully inserted")

        else:
            print("Error! cannot create the database connection")
    except sqlite3.Error as error:
        print("\n error while connecting to sqlite",error)

    #finally close the db
    finally:
        if(db):
            db.close()
            print("\n db is closed now")



def writeTofile(data, filename):
    #first convert binary dataread from the store to a proper format
    with open(filename,'wb') as file:
        file.write(data)

        try:
            image = Image.open(io.BytesIo(data))
            np_image = np.asarray(image,dtype = np.unit8)
            cv2.imwrite("m.png", np_image)
        except ValueError as e:
            print(e)
        except Error:
            print(Error)
        print("stored data to file successfully")    

def readBlob (db, empid) :
    try:
        cursor = db.cursor ()
        sql_fetch_blob_query = ''' SELECT * from new employee where id = ? '''
        cursor.execute (sql_fetch_blob_query, (empid,))# note the second argumet is a tuple
        record = cursor.fetchall()
        for row in record:
            print('id = ', row[1], 'name = ', row[1])
            name = row[1]
            photo = row[2]

            print('writing data to disk')
            path = "G:\inputs\Image_Databases\standard\\'+name+'.png'
            writeTofile(photo, path)

            cursor.close()
        return True
    except sqlite3.Error as error:
        print(error)
        return False
            
def readDB(db_file, empid):
    try:
        db = create_connection(db_file)
        if(db is not None):
            if(not readDB(db,empid)):
                raise Exception("raised exception during read from db")
    except:
        print("\n error reading from db")
    #close the db finally
    finally:
        if(db):
            db.close()
            print("\n db is closed")




#main function
if __name__ == '__main__':
    db_file = r"C:\Users\Manoj\AppData\Local\Programs\Python\Python39\mywork\SQLite_image_storage_demo.db"
    #insert data to this new database
    insert_DB(db_file) #this will insert data to database sqlite3

    #empid = employeeid
    empid = 1
    readDB(db_file,empid)
    
