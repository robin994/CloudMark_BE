from Model.PresenceModel import PresenceModel
from DB.DBUtility import DBUtility

def getPresence():
    conn = DBUtility.getLocalConnection()
    cursor = conn.cursor()
    cursor.execute("select * from presenza")
    return cursor.fetchone()

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
    
