import hashlib
import logging
import os
from uuid import uuid4

import jwt
from Dao.CallBackResponse import CallBackResponse
from Model.AccountModel import NewAccountModel
from DB.DBUtility import DBUtility
from dotenv import load_dotenv
from Model.AccountModel import AccountModel
from Model.UserModel import ResetPasswordModel, SessionModel, SuperModel, UserModel
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
                id_tipo_account=row[3]
            )
            lista_account[row[0]] = account
        if connection.is_connected():
            connection.close()
            logging.info("Chiudo la connessione")
        logging.info("ritorno lista account")

        return CallBackResponse.success(lista_account)

    @staticmethod
    def getAccountByID(id_account):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "SELECT `id_account`, `user`, `abilitato`, `id_tipo_account` FROM account WHERE `id_account` = %s;"
        val = (str(id_account),)
        cursor.execute(query, val)
        record = cursor.fetchone()
        if(record is None):
            return ""
        else:
            account = AccountModel(
                id_account=record[0],
                user=record[1],
                abilitato=record[2],
                id_tipo_account=record[3]
            )
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(account)

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
               account.id_tipo_account, key_from_password_hashed)
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
        return CallBackResponse.success(uuid)

    @staticmethod
    def deleteAccountByID(id_account):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM `account` WHERE `id_account` = '{id_account}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(id_account)

    @staticmethod
    def updateAccount(account: AccountModel, session_encoded: str):
        if AccountDao.jwt_verify(session_encoded):
            connection: MySQLConnection = DBUtility.getLocalConnection()
            cursor: MySQLCursor = connection.cursor()
            sql = "UPDATE `account` SET `user`=%s   WHERE `id_account`= %s;"
            val = (account.user, account.id_account)
            account_updated = AccountDao.getAccountByID(account.id_account)
            cursor.execute(sql, val)
            connection.commit()
            return CallBackResponse.success(account_updated)

    @staticmethod
    def resetPassword(rt: ResetPasswordModel):
        if AccountDao.jwt_verify(rt.session_admin):
            connection: MySQLConnection = DBUtility.getLocalConnection()
            cursor: MySQLCursor = connection.cursor()
            sql = """SELECT a.id_account 
                    from account a 
                    join account_dipendente ad on ad.id_account = a.id_account
                    join dipendente d on ad.id_dipendente= d.id_dipendente
                    where d.id_dipendente = %s"""
            val = (rt.id_employee,)
            cursor.execute(sql, val)
            record = cursor.fetchone()
            if (record is not None):
                password_hashed = hashPassword(rt.password_employee)
                salt_from_password_hashed = password_hashed[:32]
                rt.password_employee = key_from_password_hashed = password_hashed[32:]
                cursor: MySQLCursor = connection.cursor()
                query = "UPDATE `account` SET `password`=%s where id_account = %s;"
                val = (key_from_password_hashed, record[0],)
                cursor.execute(query, val)
                connection.commit()
                sql = "UPDATE saltini SET salt = %s;"
                val = (salt_from_password_hashed,)
                cursor.execute(sql, val)
                connection.commit()
                return CallBackResponse.success(record[0])
            return CallBackResponse.bad_request("id utente non trovato")

    @staticmethod
    def getSession(User: UserModel):

        load_dotenv()
        JWTPSW = os.getenv("JWTPSW")

        connection: MySQLConnection = DBUtility.getLocalConnection()
        session = None
        cursor: MySQLCursor = connection.cursor()
        if checkPassword(User) is True:
            sql = """SELECT 
                    a.id_account, 
                    user, 
                    abilitato, 
                    a.id_tipo_account, 
                    nome_tipo_account, 
                    lista_funzioni_del_profilo 
                FROM account a 
                JOIN tipo_account ta ON a.id_tipo_account = ta.id_tipo_account
                where user = %s;"""
            val = (User.user,)
            cursor.execute(sql, val)
            record = cursor.fetchone()
            if record[4] == 'super':
                session = SuperModel(
                    id_account=record[0],
                    user=record[1],
                    abilitate=record[2],
                    accountType=record[3],
                    accountTypeName=record[4],
                    accountListFunction=record[5],
                )
            sql = """
                SELECT 
                    a.id_account, 
                    user, 
                    abilitato, 
                    a.id_tipo_account, 
                    nome_tipo_account, 
                    lista_funzioni_del_profilo, 
                    d.id_dipendente, 
                    d.nome, 
                    d.cognome, 
                    d.email, 
                    d.telefono,
                    az.nome,
                    az.p_iva,
                    az.indirizzo,
                    az.cap,
                    az.iban,
                    az.telefono,
                    az.email,
                    az.pec,
                    az.fax
                FROM account a 
                JOIN tipo_account ta ON a.id_tipo_account = ta.id_tipo_account
                JOIN account_dipendente ad ON ad.id_account = a.id_account 
                JOIN dipendente d ON d.id_dipendente = ad.id_dipendente
                JOIN dipendente_azienda da ON d.id_dipendente = da.id_dipendente
                JOIN azienda az ON az.id_azienda = da.id_azienda
                WHERE user = %s;
            """

            cursor.execute(sql, val)
            record = cursor.fetchone()
            if(record is None and session is None):
                return CallBackResponse.bad_request("No entity found")
            elif session is None:
                session = SessionModel(
                    id_account=record[0],
                    user=record[1],
                    abilitate=record[2],
                    accountType=record[3],
                    accountTypeName=record[4],
                    accountListFunction=record[5],
                    id_employee=record[6],
                    employee_first_name=record[7],
                    employee_last_name=record[8],
                    employee_email=record[9],
                    employee_phone_number=record[10],
                    business_name=record[11],
                    business_p_iva=record[12],
                    business_address=record[13],
                    business_cap=record[14],
                    business_iban=record[15],
                    business_phone=record[16],
                    business_email=record[17],
                    business_pec=record[18],
                    business_fax=record[19]

                )
            if connection.is_connected():
                connection.close()

            session_encoded = jwt.encode(
                session.dict(), JWTPSW, algorithm="HS256")
            return CallBackResponse.success(session_encoded)
        else:
            return CallBackResponse.bad_request("User or password")

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
            return CallBackResponse.success("True")
        except Exception as err:
            logging.error(err)
            return CallBackResponse.success("False")


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
