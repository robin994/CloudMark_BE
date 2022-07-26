import mysql.connector
import json
import logging

class DBUtility:

    @staticmethod
    def getLocalConnection():

        logging.info("creo la connessione")
        with open('DB/DbLocalCredential.json') as f:
         db = json.load(f)

         # Connessione a MySQL
        connessione = mysql.connector.connect(
         # Params
        host = db['endpoint'],
        user = db['user'],
        password = db['password'],
        database = db['database'])
        logging.info("connessione eseguita correttamente")
        
        return connessione
    



