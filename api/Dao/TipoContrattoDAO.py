from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.TipoContratto import TipoContratto
from DB.DBUtility import DBUtility


class TipoContrattoDAO:
    @staticmethod
    def getAllTipoContratto():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_tipoContratto = list()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute("SELECT nome_tipocontratto, descrizione FROM tipo_contratto;")
        records = cursor.fetchall()
        for row in records:
            tipoContratto = TipoContratto(
                name=row[0], info=row[1]
            )
            lista_tipoContratto.append(tipoContratto)
        if connection.is_connected():
            connection.close()
        
        return lista_tipoContratto

    @staticmethod
    def getTipoContrattoByID(nome_tipo: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        tipoContratto = TipoContratto()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT nome_tipocontratto, descrizione FROM tipo_contratto WHERE nome_tipocontratto = '{nome_tipo}';")
        record = cursor.fetchone()
        if(record is None):
            return tipoContratto
        else:
            tipoContratto = TipoContratto(
                name=record[0], info=record[1])
        if connection.is_connected():
            connection.close()
        
        return tipoContratto

    @staticmethod
    def createTipoContratto(tipoContratto: TipoContratto):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"INSERT INTO tipo_contratto(nome_tipocontratto, descrizione) VALUES('{tipoContratto.name}','{tipoContratto.info}')")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoContratto

    @staticmethod
    def updateTipoContrattoById(tipoContratto: TipoContratto):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE tipo_contratto SET nome_tipocontratto = '{tipoContratto.name}', descrizione = '{tipoContratto.info}' WHERE nome_tipocontratto = '{tipoContratto.name}';")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoContratto

    @staticmethod
    def deleteTipoContrattoById(nometipo: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"delete from tipo_contratto where nome_tipocontratto = '{nometipo}';")
        connection.commit()
        if connection.is_connected():
           connection.close()