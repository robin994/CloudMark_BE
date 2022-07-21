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
            "select * from tipo_presenza")
        records = cursore.fetchall()
        for row in records:
            tipoPresenza = PresenceType(
                id_presenceType=row[0], name=row[1], percentageIncrease=row[2], hourlyPay=row[3])
            typePresenceList.append(tipoPresenza)
        if connection.is_connected():
            connection.close()

        return typePresenceList

    @staticmethod
    def getPresenceTypebyId(idPresenceType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        typePresence = PresenceType()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"select * from tipo_presenza tp where tp.id_tipo_presenza = '{idPresenceType}'")
        record = cursore.fetchone()
        if(record is None):
            return typePresence
        else:
            tipoPresenza = PresenceType(
                id_tipoPresenza=record[0], nomeTipoPresenza=record[1], percentualeMaggiorazione=record[2], pagaOraria=record[3])
        if connection.is_connected():
            connection.close()

        return tipoPresenza

    @staticmethod
    def createPresenceType(typePresence: PresenceType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"Insert into tipo_presenza(nome_tipo_presenza,perc_maggiorazione_paga_oraria,paga_oraria) values('{typePresence.name}','{typePresence.percentageIncrease}','{typePresence.hourlyPay}')")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return typePresence

    @staticmethod
    def updatePresenceType(typePresence: PresenceType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"update tipo_presenza set nome_tipo_presenza = '{typePresence.name}', perc_maggiorazione_paga_oraria = '{typePresence.percentageIncrease}', paga_oraria = '{typePresence.hourlyPay}' where id_tipo_presenza = {typePresence.id_presenceType};")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return typePresence

    @staticmethod
    def deletePresenceType(id_presenceType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"delete from tipo_presenza where id_tipo_presenza = {id_presenceType};")
        connection.commit()
        if connection.is_connected():
            connection.close()
