from mysql.connector.connection import MySQLConnection
from Model.OrderEmployeeModel import NewOrderEmployee, OrderEmployeeModel, UpdateOrderEmployeeModel, graphPayloadModel
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

    @staticmethod
    def getAllEmployeeByIdBusiness(params: graphPayloadModel):
        connection = DBUtility.getLocalConnection()
        order_employee_list = list()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT c.id_commessa, c.id_dipendente, SUM(c.rate) , da.data_inizio_rapporto, da.data_fine_rapporto
        FROM commessa_dipendente c
        JOIN dipendente_azienda da on da.id_azienda = c.id_dipendente
        GROUP BY FORMAT(date,'yy.MM')
        where da.id_azienda = %s"""
        val = (params.id_business,)
        cursor.execute(sql, val)
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

    @staticmethod
    def addOrderToEmployee(params: NewOrderEmployee):
        connection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """INSERT into commessa_dipendente(id_commessa, id_dipendente, rate) VALUES (%s, %s, %s)"""
        val = (params.id_order, params.id_employee, params.rate,)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(params)

    @staticmethod
    def deleteOrderToEmployee(params: OrderEmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """Delete from commessa_dipendente where id_commessa= %s AND id_dipendente = %s"""
        val = (params.id_order, params.id_employee,)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(params)

    @staticmethod
    def updateOrderToEmployee(params: UpdateOrderEmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """UPDATE commessa_dipendente SET id_commessa = %s, id_dipendente = %s , rate = %s where id_commessa = %s and id_dipendente = %s"""
        val = (params.new_order.id_order, params.new_order.id_employee,
               params.new_order.rate, params.old_order.id_order, params.old_order.id_employee,)
        try:
            cursor.execute(sql, val)
            connection.commit()
        except connection.Error as error:
            return CallBackResponse.error(error)
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(params)
