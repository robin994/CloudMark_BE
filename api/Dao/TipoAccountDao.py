from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.TipoAccount import TipoAccount
from DB.DBUtility import DBUtility

# testati e funzionanti
class TipoAccountDao:
    @staticmethod
    def getAllTipoAccount():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_tipoAccount = dict()
        cursore: MySQLCursor = connection.cursor()
        query = "SELECT ta.id_tipoAccount, ta.nome_tipoAccount, ta.lista_funzioni_del_profilo FROM tipoaccount ta"
        cursore.execute(query)
        records = cursore.fetchall()
        for row in records:
            tipoAccount = TipoAccount(
                id_tipoAccount=row[0],
                nomeTipoAccount=row[1],
                funzioneProfilo=row[2])
            lista_tipoAccount[row[0]] = tipoAccount
        if connection.is_connected():
            connection.close()
        
        return lista_tipoAccount

    @staticmethod
    def getTipoAccountByIdTipoAccount(id_tipoAccount: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        tipoAccount = TipoAccount()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"SELECT ta.id_tipoAccount,ta.nome_tipoAccount, ta.lista_funzioni_del_profilo FROM tipoaccount ta WHERE ta.id_tipoAccount = {id_tipoAccount}")
        record = cursore.fetchone()
        if(record is None):
            return tipoAccount
        else:
            tipoAccount = TipoAccount(
                id_tipoAccount=record[0],
                nomeTipoAccount=record[1],
                funzioneProfilo=record[2])
        if connection.is_connected():
            connection.close()
        
        return tipoAccount

    @staticmethod
    def createTipoAccount(tipoAccount: TipoAccount):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"Insert into tipoaccount(nome_tipoAccount,lista_funzioni_del_profilo) values('{tipoAccount.nomeTipoAccount}','{tipoAccount.funzioneProfilo}')")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoAccount

    @staticmethod
    def updateTipoAccount(tipoAccount: TipoAccount):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"update tipoaccount set nome_tipoAccount='{tipoAccount.nomeTipoAccount}', lista_funzioni_del_profilo = '{tipoAccount.funzioneProfilo}' where id_tipoAccount = '{tipoAccount.id_tipoAccount}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoAccount

    @staticmethod
    def deleteTipoAccount(id_tipoAccount: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"delete from tipoaccount where id_tipoAccount = '{id_tipoAccount}'")
        connection.commit()
        if connection.is_connected():
           connection.close()
        
        return f"TipoAccount con nome = {id_tipoAccount} eliminato"
