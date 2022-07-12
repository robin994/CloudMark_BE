from DB.DBUtility import DBUtility 
from Model.BusinessModel import BusinessModel

class BusinessDao:
    
    @staticmethod
    def getAllBusiness():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM azienda""")
        return cursor.fetchall()
    
    @staticmethod
    def getBusinessByID(AccountID):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM azienda Where id_azienda == %s", id)
        return cursor.fetchone()

    @staticmethod
    def addBusiness(business: BusinessModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO azienda(id_azienda, nome, p_iva, iban, indirizzo, telefono, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                business['id'],
                                business['name'],
                                business['p_iva'],
                                business['iban'],
                                business['address'],
                                business['phone'],
                                business['email']
                        ))
        return cursor.fetchall()