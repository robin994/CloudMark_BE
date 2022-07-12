import logging
import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.OrderModel import OrderModel
import sys
sys.path.insert(0, 'back-end/api/DB')
from DBUtility import DBUtility

class CommessaDAO:

    @staticmethod
    def getAllOrders():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM commessa""")
        return cursor.fetchall()
    
    @staticmethod
    def getEmployeesByID(AccountID):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM commessa Where id_commessa == %s", id)
        return cursor.fetchone()

    @staticmethod
    def createAccount(commessa:OrderModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO commessa(id_dipendente, descrizione, id_cliente, id_azienda, data_inizio, data_fine) VALUES(%s, %s, %s, %s, %s, %s); COMMIT;", (
                                commessa['id'],
                                commessa['descrizione'],
                                commessa['id_cliente'],
                                commessa['id_azienda'],
                                commessa['data_inizio'],
                                commessa['data_fine']    
                        ))
        return cursor.fetchall()  