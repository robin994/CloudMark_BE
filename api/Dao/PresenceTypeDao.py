from unicodedata import name
from DB.DBUtility import DBUtility
from Model.PresenceType import PresenceType
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor


class PresenceTypeDao:
    @staticmethod
    def getAllPresenceType():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        typePresenceList = list()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            "SELECT * FROM tipo_presenza")
        records = cursore.fetchall()
        for row in records:
            tipoPresenza = PresenceType(
                id_presence_type=row[0], name=row[1], percentage_increase=row[2], hourly_pay=row[3])
            typePresenceList.append(tipoPresenza)
        if connection.is_connected():
            connection.close()

        return typePresenceList

    @staticmethod
    def getPresenceTypebyId(id_presence_type: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        typePresence = PresenceType()
        cursore: MySQLCursor = connection.cursor()
        sql = "SELECT * FROM tipo_presenza tp WHERE tp.id_tipo_presenza = %s"
        val = (id_presence_type,)
        cursore.execute(sql, val)
        record = cursore.fetchone()
        if(record is None):
            return typePresence
        else:
            tipo_presenza = PresenceType(
                id_presence_type=record[0], name=record[1], percentage_increase=record[2], hourly_pay=record[3])
        if connection.is_connected():
            connection.close()

        return tipo_presenza

    @staticmethod
    def createPresenceType(typePresence: PresenceType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = "INSERT into tipo_presenza(nome_tipo_presenza,perc_maggiorazione_paga_oraria,paga_oraria) VALUES (%s, %s, %s)"
        val = (typePresence.name, typePresence.percentage_increase, typePresence.hourly_pay)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return typePresence

    @staticmethod
    def updatePresenceType(typePresence: PresenceType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        sql = "UPDATE tipo_presenza SET nome_tipo_presenza = %s, perc_maggiorazione_paga_oraria = %s, paga_oraria = %s WHERE id_tipo_presenza = %s"
        val = (typePresence.name, typePresence.percentage_increase, typePresence.hourly_pay, typePresence.id_presence_type)
        cursore.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return typePresence

    @staticmethod
    def deletePresenceType(id_presenceType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        sql = "DELETE from tipo_presenza WHERE id_tipo_presenza = %s"
        val = (id_presenceType,)
        cursore.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
