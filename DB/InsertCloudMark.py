import logging
from DBUtility import DBUtility
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection


class InsertRecord:
    def main():
        connessione: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connessione.cursor()
        with open("api/DB/utility/insert_records.sql",'r') as f:
            query = f.read()
        logging.warning("Sto inserendo i campi nel DB") 
        cursor.execute(query, multi=True)
        cursor.fetchall() 
        if connessione.is_connected:
            connessione.close()
            


if __name__ == "__main__":
    InsertRecord.main()
