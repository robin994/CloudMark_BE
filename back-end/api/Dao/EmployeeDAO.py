import logging
import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.EmployeeModel import EmployeeModel
import sys
sys.path.insert(0, 'back-end/api/DB')
from DBUtility import DBUtility

class EmployeeDAO:

    @staticmethod
    def getAllEmployees():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente""")
        return cursor.fetchall()
    
    @staticmethod
    def getEmployeesByID(AccountID):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dipendente Where id_dipendente == %s", id)
        return cursor.fetchone()

    @staticmethod
    def createAccount(dipendente:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dipendente(id_dipendente, nome, cognome, cf, iban, email, telefono,) VALUES(%s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                dipendente['id'],
                                dipendente['nome'],
                                dipendente['cognome'],
                                dipendente['cf'],
                                dipendente['iban'],
                                dipendente['email'],
                                dipendente['telefono']
                        ))
        return cursor.fetchall()
