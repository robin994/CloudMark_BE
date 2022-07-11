import mysql.connector
import json
import logging

class DBUtility:

    @staticmethod
    def getLocalConnection():
<<<<<<< HEAD
        print("creo la connessione")
        with open("CloudMark/back-end/API/DB/DbCredential.json") as f:
         db = json.load(f) 
         connessione=None      
=======
        logging.info("creo la connessione")
        with open('./back-end/API/DB/DbCredential.json') as f:
         db = json.load(f)
         connessione=None
>>>>>>> fc846ddc01a797c290efe0fd7421403628f1026f
        try:
             # Connessione a MySQL
            connessione = mysql.connector.connect(
             # Params
            host = db['endpoint'],
            user = db['user'],
            password = db['password'],
            database = db['database'])
            logging.info("connessione eseguita correttamente")
        except mysql.connector.Error as e:
            logging.error("Error reading data from MySQL table", e)
        return connessione
    
