from operator import truediv
import dotenv
# from sqlalchemy import true
from DB.DBUtility import DBUtility 
from Model.AccountModel import AccountModel
from Model.UserModel import UserModel, SessionModel
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection
import os
import hashlib
from dotenv import load_dotenv
import jwt

# testati e funzionanti
class AccountDao:
    @staticmethod
    def getAllAccounts():
        connection : MySQLConnection = DBUtility.getLocalConnection()
        lista_account = dict()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("SELECT id_account, user, password, abilitato, id_tipoAccount FROM account")
        records = cursor.fetchall()
        for row in records:
            account = AccountModel(
                id_account=row[0],
                user=row[1],
                password=row[2],
                abilitato=row[3],
                id_tipoAccount=row[4]
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
        cursor.execute(f"SELECT id_account, user, password, abilitato, id_tipoAccount FROM account WHERE id_account = {id_account};")
        record = cursor.fetchone()
        if(record is None):
            return account
        else:
            account = AccountModel(
                id_account=record[0],
                user=record[1],
                password=record[2],
                abilitato=record[3],
                id_tipoAccount=record[4]
            )
        if connection.is_connected():
            connection.close()
        
        return account

    @staticmethod
    def createAccount(account:AccountModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        password_hashed = hashPassword(account.password)
        salt_from_password_hashed = password_hashed[:32]
        account.password = key_from_password_hashed = password_hashed[32:]
        #cursor.execute(f"INSERT INTO account(user, abilitato, tipo_account, password) VALUES('{account.user}', '{account.abilitato}', '{account.tipo_account}','{key_from_password_hashed}');")
        sql = "INSERT INTO account(user, abilitato, id_tipoAccount, password) VALUES( %s, %s, %s, %s)"
        val = (account.user, account.abilitato, account.id_tipoAccount, key_from_password_hashed)
        cursor.execute(sql, val)
        connection.commit()
        cursor.execute(f"SELECT id_account from account where user = '{account.user}'")
        id_account = cursor.fetchone()
        sql ="INSERT INTO saltini(id_account, salt) VALUES(%s, %s);"
        val2 = (id_account[0], salt_from_password_hashed)
        cursor.execute(sql, val2)
        #cursor.execute(f"INSERT INTO saltino(id_account, salt) VALUES('{id_account[0]}', '{salt_from_password_hashed}');")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return 1

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
        cursor.execute(f"UPDATE account SET user = '{account.user}', password ='{account.password}', abilitato = '{account.abilitato}', id_tipoAccount ={account.id_tipoAccount} WHERE id_account = {account.id_account};")
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
        if checkPassword(User) is True:
            cursor.execute(f"SELECT id_account, user, abilitato, id_tipoAccount FROM account WHERE user = '{User.user}';")
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
            hashPassword(User.password)

            session_encoded = jwt.encode( session.dict(), JWTPSW, algorithm="HS256")
            return session_encoded
        else:
            return None
    
def checkPassword(User: UserModel):
    password_to_check = User.password
    connection : MySQLConnection = DBUtility.getLocalConnection()
    cursor : MySQLCursor = connection.cursor()
    cursor.execute(f"SELECT password, salt FROM account INNER JOIN  saltini WHERE  saltini.id_account = account.id_account AND user = '{User.user}';")
    record = cursor.fetchone()
    if(record is None):
        return False
    else:
        key = record[0]
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password_to_check.encode('utf-8').strip(), # Convert the password to bytes
        record[1], 
        100000
    )

    if new_key == key:
        return True
    else:
        return False

def hashPassword(password: str):    
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8').strip(), salt, 100000)
    return salt + key 
    

