from datetime import date
from uuid import UUID, uuid4
from Model.PresenceModel import PresenceModel
from DB.DBUtility import DBUtility
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection

# testati e funzionanti


class PresenceDao:
    @staticmethod
    def getPresenceByPrimaryKey(id_employee, datePresence , id_tipoPresenza):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        presence = PresenceModel()
        cursor.execute(
            f"SELECT id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza WHERE id_dipendente = '{id_employee}' AND data = '{datePresence}' AND id_tipo_presenza = '{id_tipoPresenza}';")
        record = cursor.fetchone()
        if(record is None):
            return presence
        else:
            presence = PresenceModel(
                id_employee=record[0],
                date_presence=record[1],
                id_tipoPresenza=record[2],
                id_order=record[3],
                hours=record[4]
            )
        if connection.is_connected():
            connection.close()

        return presence

    @staticmethod
    def getAllPresence():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        cursor.execute(
            "SELECT id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza;")
        records = cursor.fetchall()
        for row in records:
            presence = PresenceModel(
                id_employee=row[0],
                date_presence=row[1],
                id_tipoPresenza=row[2],
                id_order=row[3],
                hours=row[4]
            )
            lista_presence.append(presence)
        if connection.is_connected():
            connection.close()

        return lista_presence

    @staticmethod
    def createPresence(presence: PresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = "INSERT INTO presenza(id_dipendente, data, id_tipo_presenza, id_commessa, ore) VALUES (%s, %s, %s, %s, %s);"
        val = (presence.id_employee,presence.date_presence,presence.id_tipoPresenza,presence.id_order,presence.hours)
        cursor.execute(sql,val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return presence

    @staticmethod
    def updatePresenceByIDEmployeeAndDate(presence: PresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "UPDATE presenza SET id_dipendente = %s , data = %s id_commessa = %s, ore = %s WHERE id_dipendente = %s AND data = %s AND id_tipo_presenza = '%s';"
        connection.commit()
        if connection.is_connected():
            connection.close()

        return presence

    @staticmethod
    def deletePresenceByPK(id_employee, datePresence, id_typePresence):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM presenza WHERE id_dipendente = '{id_employee}' AND data = '{datePresence}' AND id_tipo_presenza = '{id_typePresence}';")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"Presenza con id_dipendente= {id_employee}, data= '{datePresence}', id_tipoPresenza='{id_typePresence}' eliminata"
