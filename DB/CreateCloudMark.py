import json
import logging
from DBUtility import DBUtility
from mysql.connector.cursor import MySQLCursor
import mysql.connector


class CreateCloudMark:
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
        with open("DB/utility/cloudmark_db_and_tables_creation.sql", 'r') as f:
            logging.warning("Sto Creando Il DB")
            cursor: MySQLCursor = connessione.cursor()
            sql_str = f.read()
            cursor.execute(sql_str, multi=True)
        if connessione.is_connected:
            connessione.close()


if __name__ == "__main__":
    CreateCloudMark.main()
