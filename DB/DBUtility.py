import mysql.connector
import json
import logging

class DBUtility:

    @staticmethod
    def getLocalConnection():

        logging.info("creo la connessione")
        db = dict()
        db['endpoint'] = "localhost"
        db['user'] = "root"
        db['password'] = ""
        db['database'] = "cloudmark"
        try: 
            with open('DB/DbLocalCredential.json') as f:
                db = json.load(f)
        except:
            logging.info("File non trovato.")
         # Connessione a MySQL
        connessione = mysql.connector.connect(
         # Params 
        host = db['endpoint'],
        user = db['user'],
        password = db['password'],
        database = db['database'])
        logging.info("connessione eseguita correttamente")
        
        return connessione
    



