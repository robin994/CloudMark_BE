from DB.DBUtility import DBUtility
from Model.BusinessModel import BusinessModel
from mysql.connector.connection import MySQLConnection
from Model.CallBackResponse import CallBackResponse
from mysql.connector.cursor import MySQLCursor
import json

# testati e funzionanti
class BusinessDao:

    @staticmethod
    def getAllBusiness():
        connection : MySQLConnection = DBUtility.getLocalConnection()
        lista_business = dict()
        cursor : MySQLCursor= connection.cursor()
        cursor.execute("SELECT id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax FROM azienda")
        records = cursor.fetchall()
        for row in records:
            business = BusinessModel(
                id_business= row[0],
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
            lista_business[row[0]] =  business
            
        if connection.is_connected():
            connection.close()
        
        return lista_business

    @staticmethod
    def filterByBusiness(bus : BusinessModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_business = dict()
        sql = """SELECT * FROM azienda WHERE `nome` LIKE %s AND `p_iva` LIKE %s AND `indirizzo` LIKE %s AND `cap` LIKE %s 
        AND `iban` LIKE %s AND `telefono` LIKE %s AND `email` LIKE %s AND `pec` LIKE %s AND `fax` LIKE %s"""
        val = ('%'+bus.name+'%', '%'+bus.p_iva, '%'+bus.address+'%', '%'+bus.cap+'%', '%'+bus.iban+'%', '%'+bus.phone+'%', '%'+bus.email+'%', '%'+bus.pec+'%', '%'+bus.fax+'%')
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if records is None:
            response = CallBackResponse(esitoChiamata="OK", numeroRisultati=0, error="")
            lista_business['response'] = response    
        else:
            for record in records:
                business = BusinessModel(
                    id_business=record[0],
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
                response = CallBackResponse(esitoChiamata="Ok", numeroRisultati=1).dict(exclude_none=True)
                lista_business[record[0]] = business
                lista_business['response'] = response
        if connection.is_connected():
            connection.close()
        return lista_business

    # @staticmethod
    # def getBusinessByID(id_azienda: int):
    #     connection : MySQLConnection = DBUtility.getLocalConnection()
    #     business = BusinessModel()
    #     cursor : MySQLCursor = connection.cursor()
    #     cursor.execute(f"SELECT id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax FROM azienda WHERE id_azienda ='{id_azienda}'")
    #     record = cursor.fetchone()
    #     if(record is None):
    #         return business
    #     else:
    #         business = BusinessModel(
    #             id_business= record[0],
    #             name= record[1],
    #             p_iva= record[2],
    #             address= record[3],
    #             cap= record[4],
    #             iban= record[5],
    #             phone= record[6],
    #             email= record[7],
    #             pec= record[8],
    #             fax= record[9]
    #         )
    #     if connection.is_connected():
    #         connection.close()

    #     return record

    @staticmethod
    def createBusiness(business: BusinessModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"INSERT INTO azienda(nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax) VALUES('{business.name}','{business.p_iva}','{business.address}','{business.cap}','{business.iban}','{business.phone}','{business.email}','{business.pec}','{business.fax}');")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return business

    @staticmethod
    def updateBusinessById(business: BusinessModel):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        cursor : MySQLCursor = connection.cursor()
        cursor.execute(f"UPDATE azienda SET nome = '{business.name}', p_iva ='{business.p_iva}', iban = '{business.iban}', indirizzo ='{business.address}' , cap ='{business.cap}', telefono ='{business.phone}', email ='{business.email}', pec ='{business.pec}' , fax ='{business.fax}' WHERE id_azienda = {business.id_business};")
        connection.commit()
        if connection.is_connected():
            connection.close()
        return business

    @staticmethod
    def deleteBusinessById(id_business: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"delete from azienda where id_azienda = '{id_business}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return f"Azienda con id = {id_business} eliminata"

    # @staticmethod
    # def getBusinessbyName(nome:str):
    #     connection : MySQLConnection = DBUtility.getLocalConnection()
    #     business = BusinessModel()
    #     cursor : MySQLCursor = connection.cursor()
    #     cursor.execute(f"SELECT id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax FROM azienda WHERE nome ='{nome}'")
    #     record = cursor.fetchone()
    #     if(record is None):
    #         return business
    #     else:
    #         business = BusinessModel(
    #             id_business= record[0],
    #             name= record[1],
    #             p_iva= record[2],
    #             address= record[3],
    #             cap= record[4],
    #             iban= record[5],
    #             phone= record[6],
    #             email= record[7],
    #             pec= record[8],
    #             fax= record[9]
    #         )
    #     if connection.is_connected():
    #         connection.close()

    #     return record