import json
import logging
from DBUtility import DBUtility
from mysql.connector.cursor import MySQLCursor
import mysql.connector


class InsertRecord:
    def main():
        with open('DB/DbLocalCredential.json') as f:
            db = json.load(f)
        connessione=None
        connessione = mysql.connector.connect(
             # Params
            host = db['endpoint'],
            user = db['user'],
            password = db['password'],
            charset="utf8mb4")
        with open("DB/utility/insert_records.sql",'r') as f:
            query = f.read()
            logging.warning("Sto inserendo i campi nel DB")
            cursor: MySQLCursor = connessione.cursor() 
            cursor.execute(query, multi=True)
            cursor.fetchall() 
        if connessione.is_connected:
            cursor.close()
            connessione.close()
            


if __name__ == "__main__":
    InsertRecord.main()
