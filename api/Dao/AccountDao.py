from operator import truediv
from typing import Dict
from uuid import UUID, uuid4
from DB.DBUtility import DBUtility
from Model.AccountModel import AccountModel
from Model.UserModel import UserModel, SessionModel
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection
import os
import hashlib
from dotenv import load_dotenv
import jwt
import logging

from api.Model.AccountModel import NewAccountModel

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

        return account

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
        return uuid

    @staticmethod
    def deleteAccountByID(id_account: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM account WHERE id_account = {id_account}")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"Account con id = {id_account} eliminato"

    @staticmethod
    def updateAccountByID(account: AccountModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"UPDATE account SET user = '{account.user}', password ='{account.password}', abilitato = '{account.abilitato}', id_tipoAccount ={account.id_tipoAccount} WHERE id_account = {account.id_account};")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return account

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

            session_encoded = jwt.encode(
                session.dict(), JWTPSW, algorithm="HS256")
            return session_encoded
        else:
            return None


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
        return True
    else:
        return False


def hashPassword(password: str):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key
