from DB.DBUtility import DBUtility 
from Model.AccountModel import AccountModel
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection

# testati e funzionanti
class AccountDao:
    @staticmethod
    def getAllAccounts():
        connection : MySQLConnection = DBUtility.getLocalConnection()
        lista_account = list()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("SELECT id_account, user, password, abilitato, tipo_account FROM account")
        records = cursor.fetchall()
        for row in records:
            account = AccountModel(
                id_account=row[0],
                user=row[1],
                password=row[2],
                abilitato=row[3],
                tipo_account=row[4]
            )
            lista_account.append(account)
        if connection.is_connected():
            connection.close()
        
        return lista_account
    
    @staticmethod
    def getAccountByID(id_account: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        account = AccountModel()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT id_account, user, password, abilitato, tipo_account FROM account    WHERE id_account = {id_account};")
        record = cursor.fetchone()
        if(record is None):
            return account
        else:
            account = AccountModel(
                id_account=record[0],
                user=record[1],
                password=record[2],
                abilitato=record[3],
                tipo_account=record[4]
            )
        if connection.is_connected():
            connection.close()
        
        return account

    @staticmethod
    def createAccount(account:AccountModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"INSERT INTO account(user, password, abilitato, tipo_account) VALUES('{account.user}', '{account.password}', '{account.abilitato}', '{account.tipo_account}');")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return account

    @staticmethod
    def deleteAccountByID(id_account: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM account WHERE id_account = {id_account}")
        connection.commit()
        if connection.is_connected():
            connection.close()

    @staticmethod
    def updateAccountByID(account:AccountModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE account SET user = '{account.user}', password ='{account.password}', abilitato = '{account.abilitato}', tipo_account ='{account.tipo_account}' where id_account = {account.id_account};")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return account