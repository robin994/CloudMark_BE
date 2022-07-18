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
        cursor.execute("SELECT id_tipoContratto, nome_tipocontratto, descrizione FROM tipocontratto;")
        records = cursor.fetchall()
        for row in records:
            tipoContratto = TipoContratto(
                id_tipoContratto=row[0], name=row[1], info=row[2]
            )
            lista_tipoContratto.append(tipoContratto)
        if connection.is_connected():
            connection.close()
        
        return lista_tipoContratto

    @staticmethod
    def getTipoContrattoByID(id_tipoContratto: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        tipoContratto = TipoContratto()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT id_tipoContratto, nome_tipocontratto, descrizione FROM tipocontratto WHERE id_tipoContratto = {id_tipoContratto};")
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
        cursor.execute(f"INSERT INTO tipocontratto(nome_tipocontratto, descrizione) VALUES('{tipoContratto.name}','{tipoContratto.info}')")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoContratto

    @staticmethod
    def updateTipoContrattoById(tipoContratto: TipoContratto):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE tipocontratto SET nome_tipocontratto = '{tipoContratto.name}', descrizione = '{tipoContratto.info}' WHERE id_tipoContratto = '{tipoContratto.id_tipoContratto}';")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoContratto

    @staticmethod
    def deleteTipoContrattoById(id_tipoContratto: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"delete from tipocontratto where id_tipoContratto = '{id_tipoContratto}';")
        connection.commit()
        if connection.is_connected():
           connection.close()
        
        return f"TipoContratto con id = {id_tipoContratto} eliminato"