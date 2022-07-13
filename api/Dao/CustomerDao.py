from DB.DBUtility import DBUtility
from Model.CustomerModel import CustomerModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

class CustomerDao:
    
    @staticmethod
    def getCustomerByID(id: int):
        connection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente Where id_cliente == %s", id)
        return cursor.fetchone()

    @staticmethod    
    def getAllCustomers():
        connection = DBUtility.getLocalConnection()
        cursor : MySQLCursor= connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        return cursor.fetchall()

    @staticmethod  
    def addCustomer(customer: CustomerModel):
        connection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("INSERT INTO cliente(nome, p_iva, iban,cap,indirizzo, telefono, email, pec, fax) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                customer['name'],
                                customer['p_iva'],
                                customer['cap'],
                                customer['iban'],
                                customer['address'],
                                customer['phone'],
                                customer['email'],
                                customer['pec'],
                                customer['fax'],
                        ))
        return cursor.fetchall()

    @staticmethod
    def deleteCustomerByID(id):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente =" + id)
        return cursor.commit()

    @staticmethod
    def updateAccountByID(customer:CustomerModel):
        connection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute("UPDATE cliente SET nome = '%s', p_iva ='%s', iban = '%s', indirizzo ='%s' , cap ='%s' telefono ='%s' , email ='%s' , pec ='%s' , fax ='%s' where id_cliente = '%s'; COMMIT;", (
                                customer['name'],
                                customer['p_iva'],
                                customer['iban'],
                                customer['address'],
                                customer['cap'],
                                customer['phone'],
                                customer['email'],
                                customer['pec'],
                                customer['fax'],
                                customer['id']
                                

                        ))
        return cursor.fetchall()