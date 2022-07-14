from DB.DBUtility import DBUtility
from Model.CustomerModel import CustomerModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

# testati e funzionanti
class CustomerDao:
    
    @staticmethod
    def getCustomerByID(id_customer: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        customer = CustomerModel()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"SELECT id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax FROM cliente WHERE id_cliente ='{id_customer}'")
        record = cursor.fetchone()
        if(record is None):
            return customer
        else:
            customer = CustomerModel(
                id_customer= record[0],
                name= record[1],
                p_iva= record[2],
                address= record[3],
                cap= record[4],
                iban= record[5],
                phone= record[6],
                email= record[7],
                pec= record[8],
                fax= record[9]
            )
        if connection.is_connected():
            connection.close()

        return record

    @staticmethod    
    def getAllCustomers():
        connection = DBUtility.getLocalConnection()
        lista_customer = list()
        cursor : MySQLCursor= connection.cursor()
        cursor.execute("SELECT id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax FROM cliente")
        records = cursor.fetchall()
        for row in records:
            customer = CustomerModel(
                id_customer= row[0],
                name= row[1],
                p_iva= row[2],
                address= row[3],
                cap= row[4],
                iban= row[5],
                phone= row[6],
                email= row[7],
                pec= row[8],
                fax= row[9]
            )
            lista_customer.append(customer)
        if connection.is_connected():
            connection.close()
        
        return lista_customer

    @staticmethod  
    def createCustomer(customer: CustomerModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"INSERT INTO cliente(nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax) VALUES('{customer.name}','{customer.p_iva}','{customer.address}','{customer.cap}','{customer.iban}','{customer.phone}','{customer.email}','{customer.pec}','{customer.fax}');")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return customer
        
    @staticmethod
    def deleteCustomerByID(id_customer: int):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM cliente WHERE id_cliente = {id_customer}")
        connection.commit()
        if connection.is_connected():
            connection.close()

    @staticmethod
    def updateCustomerByID(customer:CustomerModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE cliente SET nome = '{customer.name}', p_iva ='{customer.p_iva}', iban = '{customer.iban}', indirizzo ='{customer.address}' , cap ='{customer.cap}', telefono ='{customer.phone}', email ='{customer.email}', pec ='{customer.pec}' , fax ='{customer.fax}' WHERE id_cliente = '{customer.id_customer}';")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return customer