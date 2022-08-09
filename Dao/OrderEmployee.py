from mysql.connector.connection import MySQLConnection
from Model.OrderEmployeeModel import NewOrderEmployee
from Dao.CallBackResponse import CallBackResponse
from mysql.connector.cursor import MySQLCursor
from DB.DBUtility import DBUtility


class OrderEmployee:
        
    @staticmethod
    def getAllEmployeeByCustomersRate():
        connection = DBUtility.getLocalConnection()
        order_employee_list = list()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT c.id_commessa, c.id_dipendente, c.rate FROM commessa_dipendente c"""
        cursor.execute(sql,)
        records = cursor.fetchall()
        for record in records:
            order_employee = NewOrderEmployee(
                id_order=record[0],
                id_employee=record[1],
                rate=record[2],
            )
            order_employee_list.append(order_employee)
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(order_employee_list)