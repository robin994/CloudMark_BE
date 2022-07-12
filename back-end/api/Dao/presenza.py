import sys
import logging
sys.path.insert(0, 'C:/Users/loryg/Desktop/progetto_bas/CloudMark/back-end/api')
from DB.DBUtility import DBUtility
def getPresenza():
    conn = DBUtility.getLocalConnection()
    
    cursor = conn.cursor()
    
    cursor.execute("select * from presenza")
    
    data = cursor.fetchone()
    
    logging.info("Connection extablished to: ", data)
    
    conn.close()
    if(data == None):
        print("this database doesn't have any data")
        return("error")
    else:
        return data

def setPresenza():
    conn = DBUtility.getLocalConnection()
        
    cursor = conn.cursor()
        
    dat1 = input("id_dipendente: ")

    dat2 = input("data: ")
        
    dat3 = input("tipo_presenza: ")
        
    dat4 = input("id_commessa: ")
        
    dat5 = input("ore: ")
        
    sqlIns = "INSERT INTO account VALUES(" + dat1 + ', "' + dat2 + '", ' + '"' + dat3 +  '", ' + dat4 + ', ' + '"' + dat5+ '"' + ")"
        
    cursor.execute(sqlIns)
    
    conn.commit()
    
