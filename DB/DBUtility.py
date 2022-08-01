import json
import logging
import os

import mysql.connector
from dotenv import load_dotenv


class DBUtility:

    @staticmethod
    def getLocalConnection():

        load_dotenv()
        HOST = os.getenv("HOST")
        USER = os.getenv("USER")
        DB = os.getenv("DB")
        PASSWORD = os.getenv("PASSWORD")

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
