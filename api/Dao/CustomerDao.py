from uuid import UUID, uuid4
from Model.CallBackResponse import CallBackResponse
from DB.DBUtility import DBUtility
from Model.CustomerModel import CustomerModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from mysql.connector.errors import Error

from api.Model.CustomerModel import NewCustomerModel

# testati e funzionanti


class CustomerDao:

    @staticmethod
    def getCustomerByID(id_customer):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql= "SELECT * FROM cliente WHERE id_cliente = %s"
        val = (id_customer,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        if connection.is_connected():
            connection.close()
        
        if(record is None):
            return {}
        else:
            customer = CustomerModel(
                id_customer=record[0],
                name=record[1],
                p_iva=record[2],
                address=record[3],
                cap=record[4],
                iban=record[5],
                phone=record[6],
                email=record[7],
                pec=record[8],
                fax=record[9]
            )
            return customer

    @staticmethod
    def getAllCustomers():
        connection = DBUtility.getLocalConnection()
        lista_customer = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM cliente")
        records = cursor.fetchall()
        for row in records:
            customer = CustomerModel(
                id_customer=row[0],
                name=row[1],
                p_iva=row[2],
                address=row[3],
                cap=row[4],
                iban=row[5],
                phone=row[6],
                email=row[7],
                pec=row[8],
                fax=row[9]
            )
            lista_customer[row[0]] = customer
        if connection.is_connected():
            connection.close()

        return lista_customer

    @staticmethod
    def createCustomer(customer: NewCustomerModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        uuid = uuid4()
        cursor.execute(
            f"INSERT INTO cliente(id_cliente,nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax) VALUES('{uuid}','{customer.name}','{customer.p_iva}','{customer.address}','{customer.cap}','{customer.iban}','{customer.phone}','{customer.email}','{customer.pec}','{customer.fax}');")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return uuid

    @staticmethod
    def deleteCustomerByID(id_customer: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = "DELETE FROM `cliente` WHERE `id_cliente` = %s"
        val = (id_customer,)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"Cliente con id = {id_customer} eliminato"

    @staticmethod
    def updateCustomerByID(customer: CustomerModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """UPDATE cliente 
        SET `nome` = %s, `p_iva` =%s, `iban` = %s,
        `indirizzo` =%s , `cap` =%s, `telefono` =%s,
        `email` =%s, `pec` =%s , `fax` =%s
        WHERE `id_cliente` = %s;"""
        val = (customer.name, customer.p_iva, customer.iban, customer.address, customer.cap, customer.phone, customer.email, customer.pec, customer.fax, customer.id_customer)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return customer.id_customer

    @staticmethod
    def getCustomerByBusinessID(id_business):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_customer = dict()
        sql = "SELECT C.id_cliente, C.nome, C.p_iva, C.indirizzo, C.cap, C.iban, C.telefono, C.email, C.pec, C.fax FROM cliente C, azienda A, azienda_cliente AC WHERE C.id_cliente = AC.id_cliente and AC.id_azienda = A.id_azienda and A.id_azienda = %s;"
        val = (id_business)
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if connection.is_connected():
                connection.close()
        if records is None:
            return {}
        else:
            for row in records:
                customer = CustomerModel(
                    id_customer=row[0],
                    name=row[1],
                    p_iva=row[2],
                    address=row[3],
                    cap=row[4],
                    iban=row[5],
                    phone=row[6],
                    email=row[7],
                    pec=row[8],
                    fax=row[9]
                    )
                lista_customer[row[0]] = customer
            

        return lista_customer
