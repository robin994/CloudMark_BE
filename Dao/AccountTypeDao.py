from uuid import uuid4
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.AccountType import AccountType
from DB.DBUtility import DBUtility
from Dao.CallBackResponse import CallBackResponse
from Model.AccountType import NewAccountType

# testati e funzionanti


class AccountTypeDao:
    @staticmethod
    def getAllAccountsType():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_accountType = dict()
        cursore: MySQLCursor = connection.cursor()
        query = "SELECT * FROM tipo_account"
        cursore.execute(query)
        records = cursore.fetchall()
        for row in records:
            tipoAccount = AccountType(
                id_account_type=row[0],
                accountTypeName=row[1],
                function=row[2])
            lista_accountType[row[0]] = tipoAccount
        if connection.is_connected():
            connection.close()
        
        return  CallBackResponse.success(lista_accountType)

    @staticmethod
    def getAccountTypeById(id_accountType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        query = "SELECT * FROM tipo_account WHERE id_tipo_account = %s;"
        val = (id_accountType, )
        cursore.execute(query, val)
        record = cursore.fetchone()
        if(record is None):
            return CallBackResponse.bad_request()
        else:
            accountType = AccountType(
                id_account_type=record[0],
                accountTypeName=record[1],
                function=record[2])
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(accountType)

    @staticmethod
    def createAccountType(accountType: NewAccountType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        account_type_create = dict()
        uuid = uuid4()
        cursor: MySQLCursor = connection.cursor()
        sql = """INSERT INTO tipo_account(id_tipo_account, nome_tipo_account, lista_funzioni_del_profilo) values(%s, %s, %s)"""
        val = (str(uuid), accountType.accountTypeName, accountType.function)
        cursor.execute(sql , val)
        connection.commit()
        account_type_create[uuid] = accountType
        if connection.is_connected():
            connection.close()
        if uuid:
            return CallBackResponse.success(uuid)
        else:
            return CallBackResponse.bad_request("")

    @staticmethod
    def updateAccountType(accountType: AccountType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        account_type_update = dict()
        cursor: MySQLCursor = connection.cursor()
        sql = """UPDATE tipo_account SET nome_tipo_account = %s, lista_funzioni_del_profilo = %s WHERE id_tipo_account = %s"""
        val = (accountType.accountTypeName, accountType.function, accountType.id_account_type)
        cursor.execute(sql, val)
        connection.commit()
        account_type_update[accountType.id_account_type] = accountType
        if connection.is_connected():
            connection.close()
        if account_type_update:
            return CallBackResponse.success(account_type_update)
        else: 
            return CallBackResponse.success('')

    @staticmethod
    def deleteAccountType(id_account_type):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"delete from tipo_account where id_tipo_account = '{id_account_type}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
        if id_account_type:
            return CallBackResponse.success(id_account_type)
        else: 
            return CallBackResponse.success('')
