from uuid import uuid4

from DB.DBUtility import DBUtility
from Model.PresenceModel import NewPresenceModel, NewPresencesModel, PresenceModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from Dao.CallBackResponse import CallBackResponse
from Model.PresenceModel import LoadPresenceModel

# testati e funzionanti


class PresenceDao:
    @staticmethod
    def getPresenceByPrimaryKey(presenceId : str, employeeId : str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "SELECT id_presenza, id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza WHERE id_presenza = %s AND id_dipendente=%s;"
        val = (str(presenceId),str(employeeId))
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
        uuid = ''
        if(record is None):
            uuid = uuid4()
            cursor.execute(f"INSERT INTO presenza(id_presenza,id_dipendente, data, id_tipo_presenza, id_commessa, ore) VALUES ('{uuid}','{presence.id_employee}','{presence.date_presence}','{presence.id_tipoPresenza}','{presence.id_order}','{presence.hours}');")
            connection.commit()
            if connection.is_connected():
             connection.close()
             CallBackResponse.success(uuid)
        if connection.is_connected():
            connection.close()
            
        return CallBackResponse.success(uuid)

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
    
    @staticmethod
    def getMonthYearPresences(payload: LoadPresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        sql = """
        SELECT * FROM presenza WHERE id_dipendente = %s AND MONTH(`data`) = %s AND YEAR(`data`) = %s;"""
        val = (payload.id_employee, payload.month, payload.year)
        cursor.execute(
            sql, val)
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
    def getPresencesByEmployee(id_employee : str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        sql = """
        SELECT * FROM presenza WHERE id_dipendente = %s;"""
        val = (id_employee,)
        cursor.execute(
            sql, val)
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
    def insert_or_delete_presence(list_presence: NewPresencesModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        payload = list_presence.presences[0]
        presence_employee_year_month = list()
        sql = """SELECT * FROM presenza WHERE id_dipendente = %s AND MONTH(data) = %s AND YEAR(data) = %s;"""
        val = (payload.id_employee, str(payload.date_presence)[5:7], str(payload.date_presence)[0:4])
        cursor.execute(sql, val)
        records = cursor.fetchall()

        for row in records:
            presence = NewPresenceModel(
                id_employee=row[1],
                date_presence=row[2],
                id_tipoPresenza=row[3],
                id_order=row[4],
                hours=row[5]
            )
            presence_employee_year_month.append(presence)

        delete = """DELETE FROM presenza WHERE id_dipendente = %s;"""
        id_del = (payload.id_employee, )
        cursor.execute(delete, id_del)
        connection.commit()
        if(payload.id_employee):
            for elem in list_presence.presences:
                PresenceDao.createPresence(elem)
            if connection.is_connected():
                connection.close()
            
            return CallBackResponse.success(list_presence.presences, description="Record inserted/updated")