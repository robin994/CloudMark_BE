import mysql.connector
import json

class DBUtility: 
    
    @staticmethod
    def getLocalConnection():
        print("creo la connessione")
        with open("CloudMark/back-end/API/DB/DbCredential.json") as f:
         db = json.load(f) 
         connessione=None      
        try:
             # Connessione a MySQL
            connessione = mysql.connector.connect(
             # Params
            host = db['endpoint'],
            user = db['user'],
            password = db['password'],
            database = db['database'])
            print("connessione eseguita correttamente")
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        return connessione
    