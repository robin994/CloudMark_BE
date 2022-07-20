from uuid import UUID, uuid4
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.OrderModel import OrderModel, NewOrderModel
from DB.DBUtility import DBUtility

# testati e funzionanti


class OrderDao:
    @staticmethod
    def getAllOrders():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_orders = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT c.id_commessa,c.descrizione,c.id_cliente,c.id_azienda,c.data_inizio,c.data_fine FROM commessa c")
        records = cursor.fetchall()
        for row in records:
            order = OrderModel(
                id_order=row[0],
                description=row[1],
                id_customer=row[2],
                id_business=row[3],
                startDate=row[4],
                endDate=row[5]
            )
            lista_orders[row[0]] = order
        if connection.is_connected():
            connection.close()

        return lista_orders

    @staticmethod
    def getOrderByID(id_order: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT * from `commessa` 
        Where `id_commessa` = %s"""
        val = (id_order,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        if(record is None):
            return order
        else:
            order = OrderModel(
                id_order=record[0],
                description=record[1],
                id_customer=record[2],
                id_business=record[3],
                startDate=record[4],
                endDate=record[5])
        if connection.is_connected():
            connection.close()

        return order

    @staticmethod
    def createOrder(order: NewOrderModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        uuid = uuid4()
        sql = """INSERT INTO `commessa`
        VALUES( %s , %s , %s , %s , %s , %s);"""
        val = (str(uuid), order.description, order.id_customer, order.id_business, order.startDate, order.endDate,)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return uuid

    @staticmethod
    def updateOrderById(order: OrderModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        sql= """update commessa 
        set `descrizione` = %s ,`id_cliente` = %s,
        `id_azienda`=%s,`data_inizio`= %s, 
        `data_fine`= %s where `id_commessa` =  %s"""
        val = (order.description, order.id_customer, order.id_business, order.startDate, order.endDate, order.id_order)
        cursore.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return order

    @staticmethod
    def deleteOrderByID(id_order: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = "DELETE FROM commessa WHERE id_commessa = %s"
        val = (id_order,)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return ""
