from unicodedata import name
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.AccountType import AccountType
from DB.DBUtility import DBUtility

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

        return lista_accountType

    @staticmethod
    def getAccountTypeById(id_accountType: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        accountType = AccountType()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"SELECT * FROM tipo_account WHERE id_tipo_account = {id_accountType}")
        record = cursore.fetchone()
        if(record is None):
            return accountType
        else:
            accountType = AccountType(
                id_account_type=record[0],
                accountTypeName=record[1],
                function=record[2])
        if connection.is_connected():
            connection.close()

        return accountType

    @staticmethod
    def createAccountType(accountType: AccountType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"Insert into tipo_account(nome_tipoAccount,lista_funzioni_del_profilo) values('{accountType.accountTypeName}','{accountType.function}')")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return accountType

    @staticmethod
    def updateAccountType(accountType: AccountType):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"update tipo_account set nome_tipoAccount='{accountType.accountTypeName}', lista_funzioni_del_profilo = '{accountType.function}' where id_tipo_account = '{accountType.id_account_type}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return accountType

    @staticmethod
    def deleteAccountType(id_account_type: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"delete from tipo_account where id_tipo_account = '{id_account_type}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"TipoAccount con nome = {id_account_type} eliminato"
