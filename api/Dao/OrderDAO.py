from Model.OrderModel import OrderModel
from DB.DBUtility import DBUtility

class CommessaDAO:

    @staticmethod
    def getAllOrders():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM commessa""")
        return cursor.fetchall()
    
    @staticmethod
    def getOrderByID(id: int):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM commessa WHERE id_commessa == %s""", (id, ))
        return cursor.fetchone()

    @staticmethod
    def createOrder(order:OrderModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO commessa(id_dipendente, descrizione, id_cliente, id_azienda, data_inizio, data_fine) VALUES(%s, %s, %s, %s, %s, %s); COMMIT;", (
                                order['id'],
                                order['descrizione'],
                                order['id_cliente'],
                                order['id_azienda'],
                                order['data_inizio'],
                                order['data_fine']    
                        ))
        return cursor.fetchall()  

    @staticmethod
    def updateOrderByID(order:OrderModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""UPDATE commessa SET descrizione = '%s', id_cliente ='%s', id_azienda = '%s', data_inizio ='%s' , data_fine ='%s' where id_commessa = '%s'; COMMIT;""", (
                                order['descrizione'],
                                order['id_cliente'],
                                order['id_azienda'],
                                order['data_inzio'],
                                order['data_fine'],
                                order['id']
                        ))
        return cursor.fetchall()    

    @staticmethod
    def deleteOrderByID(id):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM commessa WHERE id_commessa =%s""", (id, ))
        return cursor.commit()    

    @staticmethod
    def getCommessaByIdDipendente(id_dipendente: int):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT CL.nome, C.data_inizio
                        FROM cliente CL, commessa C, dipendente D, commessa_dipendente CD
                        WHERE D.id_dipendente = %s AND D.id_dipendente = CD.id_dipendente AND CD.id_commessa = C.id_commessa AND C.id_cliente = CL.id_cliente""", (id_dipendente, ))
        return cursor.fetchone()