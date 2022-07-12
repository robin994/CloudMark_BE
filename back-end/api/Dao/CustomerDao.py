from DB.DBUtility import DBUtility
from Model.CustomerModel import CustomerModel

class CustomerDao:
    
    @staticmethod
    def getCustomerByID(id: int):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente Where id_cliente == %s", id)
        return cursor.fetchone()

    @staticmethod    
    def getAllCustomers():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM cliente""")
        return cursor.fetchall()

    @staticmethod  
    def addCustomer(customer: CustomerModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cliente(id_cliente, nome, p_iva, iban, indirizzo, telefono, email, pec, fax) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                customer['id'],
                                customer['name'],
                                customer['p_iva'],
                                customer['iban'],
                                customer['address'],
                                customer['phone'],
                                customer['email'],
                                customer['pec'],
                                customer['fax'],
                        ))
        return cursor.fetchall()