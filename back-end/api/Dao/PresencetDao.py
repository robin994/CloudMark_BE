from Model.PresenceModel import PresenceModel
from DB.DBUtility import DBUtility

def getPresence():
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

def addPresemce(presence: PresenceModel):
    conn = DBUtility.getLocalConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO account(id_dipendente, data, tipo_presenza, id_commessa, ore) VALUES(%s, %s, %s, %s, %s); COMMIT;", (
                                presence['id'],
                                presence['data'],
                                presence['tipo_presenza'],
                                presence['id_commessa'],
                                presence['ore']
                        ))
    return conn.commit()
    
