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
    def createEmployee(employee:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dipendente(id_dipendente, nome, cognome, cf, iban, email, telefono,) VALUES(%s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                employee['id'],
                                employee['nome'],
                                employee['cognome'],
                                employee['cf'],
                                employee['iban'],
                                employee['email'],
                                employee['telefono']
                        ))
        return cursor.fetchall()

    @staticmethod
    def updateEmployeeByID(employee:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE dipendente SET nome = '%s', cognome ='%s', cf = '%s', iban ='%s' , email ='%s' , telefono ='%s' where id_dipendente = '%s'; COMMIT;", (
                                employee['nome'],
                                employee['cognome'],
                                employee['cf'],
                                employee['iban'],
                                employee['email'],
                                employee['telefono'],
                        ))
        return cursor.fetchall()    

    @staticmethod
    def deleteEmployeeByID(id):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM dipendente WHERE id_dipendente =" + id)
        return cursor.commit()
