import logging
from DBUtility import DBUtility
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection


class CreateSchema:
    def main():
        connessione: MySQLConnection = DBUtility.getLocalConnection()
        with open("api/DB/utility/cloudmark_db_and_tables_creation.sql", 'r') as f:
            logging.warning("Sto Creando Il DB")
            cursor: MySQLCursor = connessione.cursor()
            sql_str = f.read()
            cursor.execute(sql_str, multi=True)
        if connessione.is_connected:
            connessione.close()


if __name__ == "__main__":
    CreateSchema.main()
