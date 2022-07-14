from Model.PresenceModel import PresenceModel
from DB.DBUtility import DBUtility


class PresenceDao:
            
    @staticmethod
    def getCPresenceByID(id: int):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM presenza Where id_dipendente == %s", id)
        return cursor.fetchone()

    @staticmethod
    def getAllPresence():
        conn = DBUtility.getLocalConnection()
        cursor = conn.cursor()
        cursor.execute("select * from presenza")
        return cursor.fetchone()

    @staticmethod
    def addPresemce(presence: PresenceModel):
        conn = DBUtility.getLocalConnection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO presenza(id_dipendente, data, tipo_presenza, id_commessa, ore) VALUES(%s, %s, %s, %s, %s); COMMIT;", (
                                    presence['id'],
                                    presence['data'],
                                    presence['tipo_presenza'],
                                    presence['id_commessa'],
                                    presence['ore']
                            ))
        return conn.commit()