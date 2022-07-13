from DB.DBUtility import DBUtility 
from Model.AccountModel import AccountModel

class AccountDao:
    
    @staticmethod
    def getAllAccounts():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM account""")
        return cursor.fetchall()
    
    @staticmethod
    def getAccountByID(AccountID):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM account Where id_cliente == %s", id)
        return cursor.fetchone()

    @staticmethod
    def createAccount(account:AccountModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO account(id_account, user, password, abilitato, tipo_acount) VALUES(%s, %s, %s, %s, %s); COMMIT;", (
                                account['id'],
                                account['user'],
                                account['password'],
                                account['abilitato'],
                                account['tipo_acount']
                        ))
        return cursor.fetchall()

    @staticmethod
    def deleteAccountByID(id):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM account WHERE id_account =" + id)
        return cursor.commit()

    @staticmethod
    def updateAccountByID(account:AccountModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE account SET user = '%s', password ='%s', abilitato = '%s', tipo_acount ='%s') where id_account = '%s'; COMMIT;", (
                                account['user'],
                                account['password'],
                                account['abilitato'],
                                account['tipo_acount'],
                                account['id']
                        ))
        return cursor.fetchall()