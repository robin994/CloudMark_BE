from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.PresenceType import PresenceType
from DB.DBUtility import DBUtility


class PresenceTypeDao:
    @staticmethod
    def getAllPresenceType():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        typePresenceList = list()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            "select tp.id_tipoPresenza, tp.nome_tipoPresenza, tp.perc_maggiorazione_paga_oraria, tp.paga_oraria from tipopresenza tp")
        records = cursore.fetchall()
        for row in records:
            tipoPresenza = PresenceType(
                id_presenceType=row[0], name=row[1], percentageIncrease=row[2], hourlyPay=row[3])
            typePresenceList.append(tipoPresenza)
        if connection.is_connected():
            connection.close()

        return typePresenceList

    @staticmethod
    def getPresenceTypeabyId(idPresenceType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        typePresence = PresenceType()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"select tp.id_tipoPresenza, tp.nome_tipoPresenza, tp.perc_maggiorazione_paga_oraria, tp.paga_oraria from tipopresenza tp where tp.id_tipoPresenza = '{idPresenceType}'")
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
            f"Insert into tipopresenza(nome_tipoPresenza,perc_maggiorazione_paga_oraria,paga_oraria) values('{typePresence.name}','{typePresence.percentageIncrease}','{typePresence.hourlyPay}')")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return typePresence

    @staticmethod
    def updatePresenceType(typePresence: PresenceType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"update tipopresenza set nome_tipoPresenza = '{typePresence.name}', perc_maggiorazione_paga_oraria = '{typePresence.percentageIncrease}', paga_oraria = '{typePresence.hourlyPay}' where id_tipoPresenza = {typePresence.id_presenceType};")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return typePresence

    @staticmethod
    def deletePresenceType(id_presenceType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"delete from tipopresenza where id_tipoPresenza = {id_presenceType};")
        connection.commit()
        if connection.is_connected():
            connection.close()
