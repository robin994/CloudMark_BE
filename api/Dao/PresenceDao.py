from datetime import date
from uuid import UUID, uuid4
from Model.PresenceModel import PresenceModel
from DB.DBUtility import DBUtility
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection

from api.Model.PresenceModel import NewPresenceModel

# testati e funzionanti


class PresenceDao:
    @staticmethod
    def getPresenceByPrimaryKey(id_employee: int, datePresence: date, id_tipoPresenza: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        presence = PresenceModel()
        cursor.execute(
            f"SELECT id_dipendente, data, id_tipoPresenza, id_commessa, ore FROM presenza WHERE id_dipendente = '{id_employee}' AND data = '{datePresence}' AND id_tipoPresenza = '{id_tipoPresenza}';")
        record = cursor.fetchone()
        if(record is None):
            return presence
        else:
            presence = PresenceModel(
                id_employee=record[0],
                date_presence=record[1],
                id_tipoPresenza=record[2],
                id_order=record[3],
                ore=record[4]
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
            "SELECT id_dipendente, data, tipo_presenza, id_commessa, ore FROM presenza;")
        records = cursor.fetchall()
        for row in records:
            presence = PresenceModel(
                id_employee=row[0],
                date_presence=row[1],
                id_tipoPresenza=row[2],
                id_order=row[3],
                ore=row[4]
            )
            lista_presence.append(presence)
        if connection.is_connected():
            connection.close()

        return lista_presence

    @staticmethod
    def createPresence(presence: NewPresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO presenza(id_dipendente, data, id_tipoPresenza, id_commessa, ore) VALUES ({uuid4()}, '{presence.date_presence}', '{presence.id_tipoPresenza}', {presence.id_order}, {presence.hours});")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return presence

    @staticmethod
    def updatePresenceByIDEmployeeAndDate(presence: PresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"UPDATE presenza SET id_dipendente = {presence.id_employee}, data = '{presence.date_presence}', id_tipoPresenza = '{presence.id_tipoPresenza}', id_commessa ={presence.id_order}, ore = {presence.hours} WHERE id_dipendente = '{presence.id_employee}' AND data = '{presence.date_presence}';")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return presence

    @staticmethod
    def deletePresenceByPK(id_employee: UUID, datePresence: date, id_tipoPresenza: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM presenza WHERE id_dipendente = '{id_employee}' AND data = '{datePresence}' AND id_tipoPresenza = '{id_tipoPresenza}';")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"Presenza con id_dipendente= {id_employee}, data= '{datePresence}', id_tipoPresenza='{id_tipoPresenza}' eliminata"
