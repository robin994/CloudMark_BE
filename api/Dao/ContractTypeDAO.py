from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.ContractType import ContractType
from DB.DBUtility import DBUtility


class ContractTypeDAO:
    @staticmethod
    def getAllContractsType():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        contractTypeList = list()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT id_tipo_contratto, nome_tipo_contratto, descrizione FROM tipo_contratto;")
        records = cursor.fetchall()
        for row in records:
            tipoContratto = ContractType(
                id_contractType=row[0], name=row[1], info=row[2]
            )
            contractTypeList.append(tipoContratto)
        if connection.is_connected():
            connection.close()

        return contractTypeList

    @staticmethod
    def getContractTypeByID(id_contractType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        contractType = ContractType()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"SELECT id_tipo_contratto, nome_tipo_contratto, descrizione FROM tipo_contratto WHERE id_tipo_contratto = {id_contractType};")
        record = cursor.fetchone()
        if(record is None):
            return contractType
        else:
            contractType = ContractType(
                name=record[0], info=record[1])
        if connection.is_connected():
            connection.close()

        return contractType

    @staticmethod
    def createContractType(contractType: ContractType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO tipo_contratto(nome_tipo_contratto, descrizione) VALUES('{contractType.name}','{contractType.info}')")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return contractType

    @staticmethod
    def updateContractTypeById(contractType: ContractType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"UPDATE tipo_contratto SET nome_tipo_contratto = '{contractType.name}', descrizione = '{contractType.info}' WHERE id_tipo_contratto = '{contractType.id_contractType}';")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return contractType

    @staticmethod
    def deleteContractTypeById(id_contractType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"delete from tipo_contratto where id_tipo_contratto = '{id_contractType}';")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"TipoContratto con id = {id_contractType} eliminato"
