<<<<<<< HEAD
from uuid import UUID, uuid4
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.ContractType import ContractTypeModel, NewContractTypeModel
from DB.DBUtility import DBUtility
=======
from DB.DBUtility import DBUtility
from Model.ContractType import ContractType
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
>>>>>>> de7c8bd1336457824e88a9af148b2692bcca429f


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
            tipoContratto = ContractTypeModel(
                id_contract_type=row[0], name=row[1], info=row[2]
            )
            contractTypeList.append(tipoContratto)
        if connection.is_connected():
            connection.close()

        return {"response": contractTypeList}

    @staticmethod
    def getContractTypeByID(id_contractType: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        contractType = ContractTypeModel()
        cursor: MySQLCursor = connection.cursor()
        query = "SELECT id_tipo_contratto, nome_tipo_contratto, descrizione FROM tipo_contratto WHERE id_tipo_contratto = %s;"
        val = (str(id_contractType), )
        cursor.execute(query, val)
        record = cursor.fetchone()
        if(record is None):
            return contractType
        else:
            contractType = ContractTypeModel(
                id_contract_type=record[0], name=record[1], info=record[2])
        if connection.is_connected():
            connection.close()

        return {"response": contractType}

    @staticmethod
    def createContractType(contractType: NewContractTypeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        uuid = uuid4()
        query = "INSERT INTO tipo_contratto(id_tipo_contratto, nome_tipo_contratto, descrizione) VALUES(%s, %s, %s);"
        val = (str(uuid), contractType.name, contractType.info)
        cursor.execute(query, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return {"response": uuid}

    @staticmethod
    def updateContractTypeById(contractType: ContractTypeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "UPDATE tipo_contratto SET nome_tipo_contratto = %s, descrizione = %s WHERE id_tipo_contratto = %s;"
        val = (contractType.name, contractType.info, contractType.id_contract_type)
        cursor.execute(query, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return {"response": contractType}

    @staticmethod
    def deleteContractTypeById(id_contractType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "DELETE FROM tipo_contratto WHERE id_tipo_contratto = %s;"
        val = (str(id_contractType), )
        cursor.execute(query, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return {"response": id_contractType}
