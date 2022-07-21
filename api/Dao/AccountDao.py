import hashlib
import json
import logging
import os
from uuid import UUID, uuid4

import jwt
from api.Model.AccountModel import NewAccountModel
from DB.DBUtility import DBUtility
from dotenv import load_dotenv
from Model.AccountModel import AccountModel
from Model.UserModel import SessionModel, UserModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

# testati e funzionanti


class AccountDao:
            
    @staticmethod
    def getAllAccounts():
        logging.info("Chiamata getAllAccounts")
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_account = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT id_account, user, abilitato, id_tipo_account FROM account")
        records = cursor.fetchall()
        for row in records:
            account = dict(
                id_account=row[0],
                user=row[1],
                abilitato=row[2],
                id_tipoAccount=row[3]
            )
            lista_account[row[0]] = account
        if connection.is_connected():
            connection.close()
            logging.info("Chiudo la connessione")
        logging.info("ritorno lista account")

        return lista_account

    @staticmethod
    def getAccountByID(id_account: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"SELECT `id_account`, `user`, `abilitato`, `id_tipo_account` FROM account WHERE `id_account` = '{id_account}';")
        record = cursor.fetchone()
        if(record is None):
            return ""
        else:
            account = dict(
                id_account=record[0],
                user=record[1],
                abilitato=record[2],
                id_tipoAccount=record[3]
            )
        if connection.is_connected():
            connection.close()

        return {"response":account}

    @staticmethod
    def createAccount(account: NewAccountModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        password_hashed = hashPassword(account.password)
        salt_from_password_hashed = password_hashed[:32]
        account.password = key_from_password_hashed = password_hashed[32:]
        sql = "INSERT INTO account(id_account,user, abilitato, id_tipo_account, password) VALUES(%s, %s, %s, %s, %s)"
        uuid = uuid4()
        val = (str(uuid), account.user, account.abilitato,
               account.id_tipoAccount, key_from_password_hashed)
        cursor.execute(sql, val)
        connection.commit()
        cursor.execute(
            f"SELECT id_account from account where user = '{account.user}'")
        id_account = cursor.fetchone()
        sql = "INSERT INTO saltini(id_account, salt) VALUES(%s, %s);"
        val2 = (id_account[0], salt_from_password_hashed)
        cursor.execute(sql, val2)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return {"response":uuid}

    @staticmethod
    def deleteAccountByID(id_account: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM `account` WHERE `id_account` = '{id_account}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return {"response":id_account}

    @staticmethod
    def updateAccount(account: AccountModel, session_encoded: str):                 
        if AccountDao.jwt_verify(session_encoded):
            connection : MySQLConnection = DBUtility.getLocalConnection()
            cursor : MySQLCursor = connection.cursor()
            sql = "UPDATE `account` SET `user`=%s   WHERE `id_account`= %s;"
            val = (account.user , account.id_account)
            account_updated = AccountDao.getAccountByID(account.id_account)
            cursor.execute(sql ,val)
            connection.commit()
            return {"response":account_updated}
        
    
    @staticmethod
    def getSession(User: UserModel):

        load_dotenv()
        JWTPSW = os.getenv("JWTPSW")

        connection: MySQLConnection = DBUtility.getLocalConnection()
        session = ''
        cursor: MySQLCursor = connection.cursor()
        if checkPassword(User) is True:
            cursor.execute(f"SELECT id_account, user, abilitato, id_tipo_account FROM account WHERE user = '{User.user}';")
            record = cursor.fetchone()
            if(record is None):
                return {"response":''}
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

            session_encoded = jwt.encode(
                session.dict(), JWTPSW, algorithm="HS256")
            return {"response":session_encoded}
        else:
            return {"response":"id o password errati"}
        
    @staticmethod
    def jwt_verify(token):
        load_dotenv()
        JWTPSW = os.getenv("JWTPSW")
        jwt_options = {
            'verify_signature': True
        }
        try:
            jwt.decode(
                token,
                JWTPSW,
                algorithms=['HS256'],
                options=jwt_options
            )
            return {"response": "True"}
        except Exception as err:
            print(str(err))
            return {"response": "False"}

def checkPassword(User: UserModel):
    password_to_check = User.password
    connection: MySQLConnection = DBUtility.getLocalConnection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(
        f"SELECT password, salt FROM account INNER JOIN  saltini WHERE  saltini.id_account = account.id_account AND user = '{User.user}';")
    record = cursor.fetchone()
    if(record is None):
        return False
    else:
        key = record[0]
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password_to_check.encode('utf-8'),  # Convert the password to bytes
        record[1],
        100000
    )

    if new_key == key:
        return {"response": "True"}
    else:
        return {"response": "False"}

def hashPassword(password: str):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return {"response": salt + key}
