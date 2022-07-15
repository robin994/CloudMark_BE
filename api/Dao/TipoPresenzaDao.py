from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.TipoPresenza import TipoPresenza
from DB.DBUtility import DBUtility
import mysql.connector
import logging


class TipoPresenzaDao:
    @staticmethod
    def getAllTipoPresenza():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_tipoPresenza = list() 
        cursore: MySQLCursor = connection.cursor()
        cursore.execute("select tp.id_tipoPresenza, tp.nome_tipoPresenza, tp.perc_maggiorazione_paga_oraria, tp.paga_oraria from tipopresenza tp")
        records = cursore.fetchall()
        for row in records:
            tipoPresenza = TipoPresenza(id_tipoPresenza=row[0], nomeTipoPresenza=row[1], percentualeMaggiorazione=row[2], pagaOraria=row[3])
            lista_tipoPresenza.append(tipoPresenza)
        if connection.is_connected():
            connection.close()
        
        return lista_tipoPresenza

    @staticmethod
    def getTipoPresenzabyNomeTipoPresenza(nomeTipoPresenza: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        tipoPresenza = TipoPresenza()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"select tp.nome_tipo_presenza, tp.perc_maggiorazione_paga_oraria, tp.paga_oraria from tipo_presenza tp where tp.nome_tipo_presenza = '{nomeTipoPresenza}'")
        record = cursore.fetchone()
        if(record is None):
            return tipoPresenza
        else:
            tipoPresenza = TipoPresenza(nomeTipoPresenza=record[0], percentualeMaggiorazione=record[1], pagaOraria=record[2])
        if connection.is_connected():
            connection.close()
        
        return tipoPresenza

    @staticmethod
    def insertTipoPresenza(tipoPresenza: TipoPresenza):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"Insert into tipo_presenza(nome_tipo_presenza,perc_maggiorazione_paga_oraria,paga_oraria) values('{tipoPresenza.nomeTipoPresenza}','{tipoPresenza.percentualeMaggiorazione}','{tipoPresenza.pagaOraria}')")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoPresenza

    @staticmethod
    def updateTipoPresenza(tipoPresenza: TipoPresenza):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"update tipo_presenza set perc_maggiorazione_paga_oraria = '{tipoPresenza.percentualeMaggiorazione}',paga_oraria = '{tipoPresenza.pagaOraria}' where nome_tipo_presenza = '{tipoPresenza.nomeTipoPresenza}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
        
        return tipoPresenza

    @staticmethod
    def deleteTipoPresenza(nomeTipoPresenza: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursore: MySQLCursor = connection.cursor()
        cursore.execute(f"delete from tipo_presenza where nome_tipo_presenza = '{nomeTipoPresenza}'")
        connection.commit()
        if connection.is_connected():
            connection.close()
