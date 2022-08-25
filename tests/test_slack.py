from mysql.connector.connection_cext import CMySQLConnection
from fastapi.testclient import TestClient
from DB import DBUtility
from slack import app


def test_DBUtility():
    assert type(DBUtility.getLocalConnection()) is CMySQLConnection


def test_app():
    pass
