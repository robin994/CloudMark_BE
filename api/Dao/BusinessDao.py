from DB.DBUtility import DBUtility
from Model.BusinessModel import BusinessModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor


class BusinessDao:

    @staticmethod
    def getAllBusiness():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM azienda""")
        return cursor.fetchall()

    @staticmethod
    def getBusinessByID(id_azienda):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM azienda Where id_azienda == %s""", (id_azienda, ))
        return cursor.fetchone()

    @staticmethod
    def addBusiness(business: BusinessModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO azienda(nome, p_iva, iban, indirizzo, telefono, email,cap,pec,fax) VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s); COMMIT;", (
            business['name'],
            business['p_iva'],
            business['iban'],
            business['address'],
            business['phone'],
            business['email'],
            business['cap'],
            business['pec'],
            business['fax']
        ))
        return cursor.fetchall()

    @staticmethod
    def updateBusinessById(business: BusinessModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"update account set nome = '{business.name}',p.iva='{business.p_iva}',indirizzo='{business.address}',cap='{business.cap}',iban='{business.iban}',telefono='{business.phone}',email='{business.email}',pec='{business.pec}',fax='{business.fax}' where nome_tipo_account = '{business.id}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
            return business

    @staticmethod
    def deleteBusinessById(id_business: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"delete from azienda where id_azienda = '{id_business}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

    @staticmethod
    def getBusinessbyName(nome:str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute("""SELECT * FROM azienda A WHERE A.nome = %s;""", (nome, ))
        return cursore.fetchone()