from base_logic import create_connection, convertToBinaryData, insertBLOB, writeTofile, readBlob, readDB, delete


def Add(id,filename,path,db,):
    convertToBinaryData(filename)
    insertBLOB(id,path,db)
    
    
def Remove(id,db_file):
    delete(db_file,id)
    
    