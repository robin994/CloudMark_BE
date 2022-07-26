from unicodedata import name
from uuid import uuid4
from DB.DBUtility import DBUtility
from Model.PresenceTypeModel import PresenceTypeModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from Dao.CallBackResponse import CallBackResponse
from Model.PresenceTypeModel import NewPresenceTypeModel, PresenceTypeModel


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
            tipoPresenza = PresenceTypeModel(
                id_presence_type=row[0], name=row[1], percentage_increase=row[2], hourly_pay=row[3])
            typePresenceList.append(tipoPresenza)
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(typePresenceList)

    @staticmethod
    def getPresenceTypebyId(id_presence_type):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        sql = "SELECT * FROM tipo_presenza tp WHERE tp.id_tipo_presenza = %s"
        val = (id_presence_type,)
        cursore.execute(sql, val)
        record = cursore.fetchone()
        if(record is None):
            return CallBackResponse.bad_request()
        else:
            tipo_presenza = PresenceTypeModel(
                id_presence_type=record[0], name=record[1], percentage_increase=record[2], hourly_pay=record[3])
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(tipo_presenza)

    @staticmethod
    def createPresenceType(typePresence: NewPresenceTypeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        presence_type_create = dict()
        uuid_presence_type = uuid4()
        cursor: MySQLCursor = connection.cursor()
        sql = "INSERT into tipo_presenza(id_tipo_presenza, nome_tipo_presenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES (%s, %s, %s, %s)"
        val = (str(uuid_presence_type), typePresence.name, typePresence.percentage_increase, typePresence.hourly_pay)
        cursor.execute(sql, val)
        connection.commit()
        presence_type_create[uuid_presence_type] = typePresence
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(presence_type_create)

    @staticmethod
    def updatePresenceType(typePresence: PresenceTypeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        sql = "UPDATE tipo_presenza SET nome_tipo_presenza = %s, perc_maggiorazione_paga_oraria = %s, paga_oraria = %s WHERE id_tipo_presenza = %s"
        val = (typePresence.name, typePresence.percentage_increase, typePresence.hourly_pay, typePresence.id_presence_type)
        cursore.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(typePresence)

    @staticmethod
    def deletePresenceType(id_presence_type):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        sql = "DELETE from tipo_presenza WHERE id_tipo_presenza = %s"
        val = (id_presence_type,)
        cursore.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return CallBackResponse.success(id_presence_type)
