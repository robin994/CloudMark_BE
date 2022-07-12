import sys
import logging
sys.path.insert(0, 'C:/Users/loryg/Desktop/progetto_bas/CloudMark/back-end/api')
from DB.DBUtility import DBUtility
def getAccount():

    conn = DBUtility.getLocalConnection()
    
    cursor = conn.cursor()
    
    cursor.execute("select * from account")
    
    data = cursor.fetchone()
    
    logging.info("Connection extablished to: ", data)

    conn.close()

    if(data == "None"):
        print("this database  doesn't have any data")
        return("error")
    else:
        return data

def setAccount():
    conn = DBUtility.getLocalConnection()
        
    cursor = conn.cursor()
        
    dat1 = input("id_account: ")

    dat2 = input("user: ")
        
    dat3 = input("password: ")
        
    dat4 = input("abilitato: ")
        
    dat5 = input("tipo_account: ")
        
    sqlIns = "INSERT INTO account VALUES(" + dat1 + ', "' + dat2 + '", ' + '"' + dat3 +  '", ' + dat4 + ', ' + '"' + dat5+ '"' + ")"
        
    cursor.execute(sqlIns)
    
    conn.commit()

