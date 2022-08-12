import json
import logging
import os

import mysql.connector
from dotenv import load_dotenv


class DBUtility:

    @staticmethod
    def getLocalConnection():

        load_dotenv()
        HOST = os.getenv("MYSQL_HOST")
        USER = os.getenv("MYSQL_USER")
        DB = os.getenv("MYSQL_DATABASE")
        PASSWORD = os.getenv("MYSQL_PASSWORD")

        logging.info("creo la connessione")
        db = dict()
        # Connessione a MySQL
        connessione = mysql.connector.connect(
            # Params
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB)
        logging.info("connessione eseguita correttamente")

        return connessione
