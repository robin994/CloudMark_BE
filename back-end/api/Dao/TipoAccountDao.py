from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.TipoAccount import TipoAccount
from DB.DBUtility import DBUtility
import mysql.connector
import logging

class TipoAccountDao:
    @staticmethod
    def getAllTipoAccount():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista = list()
        try:
            cursore: MySQLCursor = connection.cursor()
            query = "select ta.nome_tipo_account, ta.funzione_profilo from tipo_account ta "
            cursore.execute(query)
            records = cursore.fetchall()
            for row in records:
                tipoAccount = TipoAccount(
                    nomeTipoAccount=row[0], funzioneProfilo=row[1])
                lista.append(tipoAccount)
            return lista
        except mysql.connector.Error as e:
            logging.error("\nError reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()

    @staticmethod
    def getTipoAccountByNomeTipoAccount(nomeTipoAccount: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        try:
            cursore: MySQLCursor = connection.cursor()
            cursore.execute(
                f"select ta.nome_tipo_account, ta.funzione_profilo from tipo_account ta where ta.nome_tipo_account = '{nomeTipoAccount}'")
            record = cursore.fetchone()
            if(record is None):
                tipoAccount = TipoAccount()
                return tipoAccount
            else:
                tipoAccount = TipoAccount( nomeTipoAccount=record[0], funzioneProfilo=record[1])
            return tipoAccount
        except mysql.connector.Error as e:
            logging.error("\nError reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()

    @staticmethod
    def insertTipoAccount(tipoAccount: TipoAccount):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        try:
            cursore: MySQLCursor = connection.cursor()
            cursore.execute(
                f"Insert into tipo_account(nome_tipo_account,funzione_profilo) values('{tipoAccount.nomeTipoAccount}','{tipoAccount.funzioneProfilo}')")
            connection.commit()
            return tipoAccount
        except mysql.connector.Error as e:
            logging.error("\nError reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()

    @staticmethod
    def updateTipoAccount(tipoAccount: TipoAccount):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        try:
            cursore: MySQLCursor = connection.cursor()
            cursore.execute(
                f"update tipo_account set funzione_profilo = '{tipoAccount.funzioneProfilo}' where nome_tipo_account = '{tipoAccount.nomeTipoAccount}'")
            connection.commit()
            return tipoAccount
        except mysql.connector.Error as e:
            logging.error("\nError reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()

    @staticmethod
    def deleteTipoAccount(nomeTipoAccount: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        try:
            cursore: MySQLCursor = connection.cursor()
            cursore.execute(
                f"delete from tipo_account where nome_tipo_account = '{nomeTipoAccount}'")
            connection.commit()
        except mysql.connector.Error as e:
            logging.error("\nError reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
           
           
    