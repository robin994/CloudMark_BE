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
        cursor.execute("INSERT INTO cliente(id_account, user, password, abilitato, tipo_acount) VALUES(%s, %s, %s, %s, %s); COMMIT;", (
                                account['id'],
                                account['user'],
                                account['password'],
                                account['abilitato'],
                                account['tipo_acount']
                        ))
        return cursor.fetchall()