import dotenv
from DB.DBUtility import DBUtility 
from Model.AccountModel import AccountModel
from Model.UserModel import UserModel, SessionModel
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection
import os
from dotenv import load_dotenv
import jwt
import json


# testati e funzionanti
class AccountDao:
    @staticmethod
    def getAllAccounts():
        connection : MySQLConnection = DBUtility.getLocalConnection()
        lista_account = dict()
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
            lista_account[row[0]] = account
        if connection.is_connected():
            connection.close()
        
        return lista_account
    
    @staticmethod
    def getAccountByID(id_account: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        account = AccountModel()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT id_account, user, password, abilitato, tipo_account FROM account WHERE id_account = {id_account};")
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
        
        return f"Account con id = {id_account} eliminato"

    @staticmethod
    def updateAccountByID(account:AccountModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE account SET user = '{account.user}', password ='{account.password}', abilitato = '{account.abilitato}', tipo_account ='{account.tipo_account}' WHERE id_account = {account.id_account};")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return account
    
    @staticmethod
    def getSession(User: UserModel):
        
        load_dotenv()
        JWTPSW = os.getenv("JWTPSW")
        
        connection : MySQLConnection = DBUtility.getLocalConnection()
        session = ''
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT id_account, user, abilitato, tipo_account FROM account WHERE user = '{User.user}' AND password = '{User.password}';")
        record = cursor.fetchone()
        if(record is None):
            return ''
        else:
            session = SessionModel(
                id_account=record[0],
                user=record[1],
                abilitato=record[2],
                tipo_account=record[3]
            )
        if connection.is_connected():
            connection.close()
      
        session_encoded = jwt.encode( session.dict(), JWTPSW, algorithm="HS256")
        return session_encoded
