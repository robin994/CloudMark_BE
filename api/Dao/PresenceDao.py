from uuid import uuid4

from DB.DBUtility import DBUtility
from Model.PresenceModel import NewPresenceModel, PresenceModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from api.Dao.CallBackResponse import CallBackResponse

# testati e funzionanti


class PresenceDao:
    @staticmethod
    def getPresenceByPrimaryKey(presenceId : str, employeeId : int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "SELECT id_presenza, id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza WHERE id_presenza = %s AND id_dipendente=%s;"
        val = (presenceId,employeeId)
        cursor.execute(query,val)
        record = cursor.fetchone()
        if(record is None):
            return CallBackResponse.bad_request(presence)
        else:
            presence = PresenceModel(
                id_presence= record[0],
                id_employee=record[1],
                date_presence=record[2],
                id_tipoPresenza=record[3],
                id_order=record[4],
                hours=record[5]
            )
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(presence)

    @staticmethod
    def getAllPresence():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        cursor.execute(
            "SELECT id_presenza, id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza;")
        records = cursor.fetchall()
        for row in records:
            presence = PresenceModel(
                id_presence=row[0],
                id_employee=row[1],
                date_presence=row[2],
                id_tipoPresenza=row[3],
                id_order=row[4],
                hours=row[5]
            )
            lista_presence.append(presence)
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(lista_presence)

    @staticmethod
    def createPresence(presence: NewPresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query="SELECT id_presenza from presenza where id_dipendente = %s AND data = %s AND id_commessa = %s"
        val = (presence.id_employee,presence.date_presence,presence.id_order)
        cursor.execute(query,val)
        record = cursor.fetchone()
        if(record is None):
            uuid = uuid4()
            cursor.execute(f"INSERT INTO presenza(id_presenza,id_dipendente, data, id_tipo_presenza, id_commessa, ore) VALUES ('{uuid}','{presence.id_employee}','{presence.date_presence}','{presence.id_tipoPresenza}','{presence.id_order}','{presence.hours}');")
            connection.commit()
            if connection.is_connected():
             connection.close()
             CallBackResponse.success(uuid)
        if connection.is_connected():
            connection.close()
            
        return CallBackResponse.success(record[0])

    @staticmethod
    def updatePresenceByIDEmployeeAndDate(presence: PresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = """UPDATE presenza SET 
                   data = %s,
                   id_tipo_presenza = %s,
                   id_commessa = %s,
                   ore = %s
                   WHERE id_presenza = %s AND id_dipendente = %s;"""
        val = (presence.date_presence,presence.id_tipoPresenza,presence.id_order,presence.hours,presence.id_presence,presence.id_employee)
        cursor.execute(query, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(presence)

    @staticmethod
    def deletePresenceByPK(id_presence:str,id_employee:str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute
        query = "DELETE FROM presenza WHERE presenza.id_presenza = %s AND presenza.id_dipendente = %s;"
        val=(id_presence,id_employee)
        cursor.execute(query,val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(id_presence)
