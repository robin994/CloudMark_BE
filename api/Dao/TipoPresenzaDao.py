from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.TipoPresenza import TipoPresenza
from DB.DBUtility import DBUtility


class TipoPresenzaDao:
    @staticmethod
    def getAllTipoPresenza():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_tipoPresenza = list() 
        cursore: MySQLCursor = connection.cursor()
        cursore.execute("select tp.id_tipoPresenza, tp.nome_tipoPresenza, tp.perc_maggiorazione_paga_oraria, tp.paga_oraria from tipopresenza tp")
        records = cursore.fetchall()
        for row in records:
            tipoPresenza = TipoPresenza(id_tipoPresenza=row[0], nomeTipoPresenza=row[1], percentualeMaggiorazione=row[2], pagaOraria=row[3])
            lista_tipoPresenza.append(tipoPresenza)
        if connection.is_connected():
            connection.close()
        
        return lista_tipoPresenza

    @staticmethod
    def getTipoPresenzabyIdTipoPresenza(IdTipoPresenza: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        tipoPresenza = TipoPresenza()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"select tp.id_tipoPresenza, tp.nome_tipoPresenza, tp.perc_maggiorazione_paga_oraria, tp.paga_oraria from tipopresenza tp where tp.id_tipoPresenza = '{IdTipoPresenza}'")
        record = cursore.fetchone()
        if(record is None):
            return tipoPresenza
        else:
            tipoPresenza = TipoPresenza(id_tipoPresenza=record[0], nomeTipoPresenza=record[1], percentualeMaggiorazione=record[2], pagaOraria=record[3])
        if connection.is_connected():
            connection.close()
        
        return tipoPresenza

    @staticmethod
    def createTipoPresenza(tipoPresenza: TipoPresenza):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"Insert into tipopresenza(nome_tipoPresenza,perc_maggiorazione_paga_oraria,paga_oraria) values('{tipoPresenza.nomeTipoPresenza}','{tipoPresenza.percentualeMaggiorazione}','{tipoPresenza.pagaOraria}')")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoPresenza

    @staticmethod
    def updateTipoPresenza(tipoPresenza: TipoPresenza):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"update tipopresenza set nome_tipoPresenza = '{tipoPresenza.nomeTipoPresenza}', perc_maggiorazione_paga_oraria = '{tipoPresenza.percentualeMaggiorazione}', paga_oraria = '{tipoPresenza.pagaOraria}' where id_tipoPresenza = {tipoPresenza.id_tipoPresenza};")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoPresenza

    @staticmethod
    def deleteTipoPresenza(id_tipoPresenza: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"delete from tipopresenza where id_tipoPresenza = {id_tipoPresenza};")
        connection.commit()
        if connection.is_connected():
            connection.close()
