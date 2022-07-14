import logging
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.OrderModel import OrderModel
from DB.DBUtility import DBUtility


class CommessaDAO:

    @staticmethod
    def getAllOrders():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista = list()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT c.id_commessa,c.descrizione,c.id_cliente,c.id_azienda,c.data_inizio,c.data_fine FROM commessa c")
        records = cursor.fetchall()
        for row in records:
            commessa = OrderModel(
                id=row[0],
                descrizione=row[1],
                id_cliente=row[2],
                id_azienda=row[3],
                data_inizio=row[4],
                data_fine=row[5]
            )
            lista.append(commessa)
        if connection.is_connected():
            connection.close()
            return lista

    @staticmethod
    def getOrderByID(id: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        commessa = OrderModel()
        cursor.execute(
            f"SELECT c.id_commessa,c.descrizione,c.id_cliente,c.id_azienda,c.data_inizio,c.data_fine from commessa c Where id_commessa ='{id}'")
        record = cursor.fetchone()
        if(record is None):
            return commessa
        else:
            commessa = OrderModel(id=record[0], descrizione=record[1], id_cliente=record[2],
                                  id_azienda=record[3], data_inizio=record[4], data_fine=record[5])
        if connection.is_connected():
            connection.close()
            return commessa

    @staticmethod
    def createOrder(order: OrderModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO commessa (descrizione, id_cliente, id_azienda, data_inizio, data_fine) VALUES('{order.descrizione}','{order.id_cliente}','{order.id_azienda}',TO_DATE({order.data_inizio},'YYYY-MM-DD'),TO_DATE({order.data_fine},'YYYY-MM-DD')")
        connection.commit()
        if connection.is_connected():
            connection.close()
            return order

    @staticmethod
    def updateTipoPresenza(order: OrderModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(
            f"update commessa set descrizione = '{order.descrizione}',id_cliente = '{order.id_cliente}',id_azienda='{order.id_azienda}',data_inizio='{order.data_inizio}', data_fine='{order.data_fine}'where nome_tipo_presenza = '{order.id}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
            return logging.warning("commessa aggiornata")

    @staticmethod
    def deleteOrderByID(id):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(f"DELETE FROM commessa WHERE id_commessa ='{id}'")
        logging.warning(f"commessa con id {id} cancellata")
        return cursor.commit()
