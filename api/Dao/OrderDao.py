from uuid import UUID, uuid4
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.CommessaModel import CommessaModel
from DB.DBUtility import DBUtility
from api.Model.CommessaModel import NewCommessaModel

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
            order = CommessaModel(
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
    def getOrderByID(id_order: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        order = CommessaModel()
        cursor.execute(
            f"SELECT c.id_commessa,c.descrizione,c.id_cliente,c.id_azienda,c.data_inizio,c.data_fine from commessa c Where id_commessa ={id_order}")
        record = cursor.fetchone()
        if(record is None):
            return order
        else:
            order = CommessaModel(id_order=record[0], description=record[1], id_customer=record[2],
                                  id_business=record[3], startDate=record[4], endDate=record[5])
        if connection.is_connected():
            connection.close()

        return order

    @staticmethod
    def createOrder(order: NewCommessaModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO commessa (id_commessa,descrizione, id_cliente, id_azienda, data_inizio, data_fine) VALUES('{uuid4()}''{order.descrizione}', '{order.id_cliente}', '{order.id_azienda}', '{order.data_inizio}', '{order.data_fine}');")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return order

    @staticmethod
    def updateOrderById(order: CommessaModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"update commessa set descrizione = '{order.description}',id_cliente = '{order.id_customer}',id_azienda='{order.id_business}',data_inizio='{order.startDate}', data_fine='{order.endDate}' where id_commessa = {order.id_order}")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return order

    @staticmethod
    def deleteOrderByID(id_order: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM commessa WHERE id_commessa = {id_order}")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return f"Commessa con id = {id_order} eliminata"
