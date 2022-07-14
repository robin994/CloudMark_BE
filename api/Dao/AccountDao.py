from DB.DBUtility import DBUtility 
from Model.AccountModel import AccountModel
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection

# testati e funzionanti
class AccountDao:
    @staticmethod
    def getAllAccounts():
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("SELECT * FROM account")
        return cursor.fetchall()
    
    @staticmethod
    def getAccountByID(id_account: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT * FROM account Where id_account = {id_account};")
        return cursor.fetchone()

    @staticmethod
    def createAccount(account:AccountModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"INSERT INTO account(user, password, abilitato, tipo_account) VALUES('{account.user}', '{account.password}', '{account.abilitato}', '{account.tipo_account}');")
        return connection.commit()

    @staticmethod
    def deleteAccountByID(id_account: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM account WHERE id_account = {id_account}")
        return connection.commit()

    @staticmethod
    def updateAccountByID(account:AccountModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE account SET user = '{account.user}', password ='{account.password}', abilitato = '{account.abilitato}', tipo_account ='{account.tipo_account}' where id_account = {account.id_account};")
        return connection.commit()