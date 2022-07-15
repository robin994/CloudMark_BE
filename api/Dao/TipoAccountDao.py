from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.TipoAccount import TipoAccount
from DB.DBUtility import DBUtility

# testati e funzionanti
class TipoAccountDao:
    @staticmethod
    def getAllTipoAccount():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_tipoAccount = list()
        cursore: MySQLCursor = connection.cursor()
        query = "SELECT ta.nome_tipo_account, ta.lista_funzioni_del_profilo FROM tipo_account ta"
        cursore.execute(query)
        records = cursore.fetchall()
        for row in records:
            tipoAccount = TipoAccount(
                nomeTipoAccount=row[0],
                funzioneProfilo=row[1])
            lista_tipoAccount.append(tipoAccount)
        if connection.is_connected():
            connection.close()
        
        return lista_tipoAccount

    @staticmethod
    def getTipoAccountByNomeTipoAccount(nomeTipoAccount: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        tipoAccount = TipoAccount()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"SELECT ta.nome_tipo_account, ta.lista_funzioni_del_profilo FROM tipo_account ta WHERE ta.nome_tipo_account = '{nomeTipoAccount}'")
        record = cursore.fetchone()
        if(record is None):
            return tipoAccount
        else:
            tipoAccount = TipoAccount(
                nomeTipoAccount=record[0], funzioneProfilo=record[1])
        if connection.is_connected():
            connection.close()
        
        return tipoAccount

    @staticmethod
    def createTipoAccount(tipoAccount: TipoAccount):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"Insert into tipo_account(nome_tipo_account,lista_funzioni_del_profilo) values('{tipoAccount.nomeTipoAccount}','{tipoAccount.funzioneProfilo}')")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoAccount

    @staticmethod
    def updateTipoAccount(tipoAccount: TipoAccount):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"update tipo_account set lista_funzioni_del_profilo = '{tipoAccount.funzioneProfilo}' where nome_tipo_account = '{tipoAccount.nomeTipoAccount}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoAccount

    @staticmethod
    def deleteTipoAccount(nomeTipoAccount: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"delete from tipo_account where nome_tipo_account = '{nomeTipoAccount}'")
        connection.commit()
        if connection.is_connected():
           connection.close()
