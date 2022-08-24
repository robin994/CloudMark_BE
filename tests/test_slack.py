from mysql.connector.connection_cext import CMySQLConnection
from DB import DBUtility


def test_DBUtility():
    print(f"Type = {type(DBUtility.getLocalConnection())}")
    assert type(DBUtility.getLocalConnection()) is CMySQLConnection
