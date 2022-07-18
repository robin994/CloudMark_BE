import mysql.connector
import json
import logging
class DBUtility:

    @staticmethod
    def getLocalConnection():

        logging.info("creo la connessione")
        with open('api\DB\DbLocalCredential.json') as f:
         db = json.load(f)
         connessione=None
        try:
             # Connessione a MySQL
            connessione = mysql.connector.connect(
             # Params
            host = db['endpoint'],
            user = db['user'],
            password = db['password'],
            database = db['database'],
            charset="utf8mb4")
            logging.info("connessione eseguita correttamente")
        except mysql.connector.Error as e:
            logging.error("Error reading data from MySQL table", e)
        return connessione
    




