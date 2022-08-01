from uuid import uuid4

from DB.DBUtility import DBUtility
from Model.PresenceModel import (LoadPresenceModel, NewPresenceModel,
                                 NewPresencesModel, PresenceFirstNameLastName,
                                 PresenceModel)
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from Dao.CallBackResponse import CallBackResponse

# testati e funzionanti


class PresenceDao:
    @staticmethod
    def getPresenceByPrimaryKey(presenceId: str, employeeId: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = "SELECT id_presenza, id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza WHERE id_presenza = %s AND id_dipendente=%s;"
        val = (str(presenceId), str(employeeId))
        cursor.execute(query, val)
        record = cursor.fetchone()
        if(record is None):
            return CallBackResponse.bad_request(presence)
        else:
            presence = PresenceModel(
                id_presence=record[0],
                id_employee=record[1],
                date_presence=record[2],
                id_tipoPresenza=record[3],
                id_order=record[4],
                hours=record[5]
            )
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(presence)

    @staticmethod
    def getAllPresenceWithFirstNameLastName():
        all_presence = list()
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT d.id_dipendente, d.nome ,
        d.cognome,tp.id_tipo_presenza,c.id_commessa, p.data,
        tp.nome_tipo_presenza ,a.nome,p.ore,a.id_azienda , p.id_presenza
        FROM presenza p JOIN dipendente d on p.id_dipendente = d.id_dipendente 
        JOIN tipo_presenza tp ON p.id_tipo_presenza = tp.id_tipo_presenza 
        JOIN commessa c  ON p.id_commessa = c.id_commessa 
        JOIN azienda a ON c.id_azienda = a.id_azienda"""
        cursor.execute(sql)
        records = cursor.fetchall()
        for row in records:
            presence = PresenceFirstNameLastName(
                id_employee=row[0],
                first_name=row[1],
                last_name=row[2],
                id_type_presence=row[3],
                id_order=row[4],
                date_presence=row[5],
                tipoPresenza=row[6],
                nome_azienda=row[7],
                hours=row[8],
                id_business=row[9],
                id_presence=row[10]
            )
            all_presence.append(presence)
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(all_presence)

    @staticmethod
    def getAllPresence():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        cursor.execute(
            "SELECT id_presenza, id_dipendente, data, id_tipo_presenza, id_commessa, ore FROM presenza;")
        records = cursor.fetchall()
        for row in records:
            presence = PresenceModel(
                id_presence=row[0],
                id_employee=row[1],
                date_presence=row[2],
                id_tipoPresenza=row[3],
                id_order=row[4],
                hours=row[5]
            )
            lista_presence.append(presence)
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(lista_presence)

    @staticmethod
    def createPresence(presence: NewPresenceModel, id_presence=None):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        if (id_presence is not None):
            query = """UPDATE `presenza`
            SET `id_dipendente` = %s, 
            `data` = %s,
            `id_tipo_presenza` = %s,
            `id_commessa` =  %s,
            `ore` = %s 
            WHERE `id_presenza` = %s"""
            val = (presence.id_employee, presence.date_presence,
                   presence.id_tipoPresenza, presence.id_order, presence.hours, id_presence,)
            cursor.execute(query, val)
            connection.commit()
            if connection.is_connected():
                connection.close()
            CallBackResponse.success(id_presence)
        else:
            uuid = uuid4()
            cursor.execute(
                f"INSERT INTO presenza(id_presenza,id_dipendente, data, id_tipo_presenza, id_commessa, ore) VALUES ('{uuid}','{presence.id_employee}','{presence.date_presence}','{presence.id_tipoPresenza}','{presence.id_order}','{presence.hours}');")
            connection.commit()
            if connection.is_connected():
                connection.close()
            return CallBackResponse.success(uuid)

    @staticmethod
    def updatePresenceByIDEmployeeAndDate(presence: PresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        query = """UPDATE presenza SET 
                   data = %s,
                   id_tipo_presenza = %s,
                   id_commessa = %s,
                   ore = %s
                   WHERE id_presenza = %s AND id_dipendente = %s;"""
        val = (presence.date_presence, presence.id_tipoPresenza, presence.id_order,
               presence.hours, presence.id_presence, presence.id_employee)
        cursor.execute(query, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(presence)

    @staticmethod
    def deletePresenceByPK(id_presence: str, id_employee: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute
        query = "DELETE FROM presenza WHERE presenza.id_presenza = %s AND presenza.id_dipendente = %s;"
        val = (id_presence, id_employee)
        cursor.execute(query, val)
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(id_presence)

    @staticmethod
    def getMonthYearPresences(payload: LoadPresenceModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        sql = """
        SELECT * FROM presenza WHERE id_dipendente = %s AND MONTH(`data`) = %s AND YEAR(`data`) = %s;"""
        val = (payload.id_employee, payload.month, payload.year)
        cursor.execute(
            sql, val)
        records = cursor.fetchall()
        for row in records:
            presence = PresenceModel(
                id_presence=row[0],
                id_employee=row[1],
                date_presence=row[2],
                id_tipoPresenza=row[3],
                id_order=row[4],
                hours=row[5]
            )
            lista_presence.append(presence)
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(lista_presence)

    @staticmethod
    def getPresencesByEmployee(id_employee: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_presence = list()
        sql = """
        SELECT * FROM presenza WHERE id_dipendente = %s;"""
        val = (id_employee,)
        cursor.execute(
            sql, val)
        records = cursor.fetchall()
        for row in records:
            presence = PresenceModel(
                id_presence=row[0],
                id_employee=row[1],
                date_presence=row[2],
                id_tipoPresenza=row[3],
                id_order=row[4],
                hours=row[5]
            )
            lista_presence.append(presence)
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(lista_presence)

    @staticmethod
    def insert_or_update_presence(payload: PresenceModel):
        print(payload)
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT * FROM presenza WHERE id_presenza = %s;"""
        val = (payload.id_presence,)
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if records is None:
            return CallBackResponse.bad_request("Dato non esistente")

        presence = NewPresenceModel(
            id_employee=payload.id_employee,
            date_presence=payload.date_presence,
            id_tipoPresenza=payload.id_tipoPresenza,
            id_order=payload.id_order,
            hours=payload.hours,
        )

        connection.commit()
        if(payload.id_employee):
            if PresenceDao.createPresence(presence, payload.id_presence).status == "ERROR":
                if connection.is_connected():
                    connection.close()
                return CallBackResponse.bad_request("Errore nella creazione")
            if connection.is_connected():
                connection.close()

        return CallBackResponse.success(presence, description="Record inserted/updated")
