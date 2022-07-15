from urllib import response
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.EmployeeModel import EmployeeModel
from DB.DBUtility import DBUtility
from Model.CallBackResponse import CallBackResponse
# testati e funzionanti


class EmployeeDAO:
    
    @staticmethod
    def getAllEmployees():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_employee = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT id_dipendente, nome, cognome, cf, iban, tipo_contratto, email, telefono FROM dipendente")
        records = cursor.fetchall()
        for row in records:
            employee = EmployeeModel(
                id_employee=row[0],
                nome=row[1],
                cognome=row[2],
                cf=row[3],
                iban=row[4],
                tipo_contratto=row[5],
                email=row[6],
                telefono=row[7]
            )
            lista_employee[row[0]] = employee
        if connection.is_connected():
            connection.close()

        return lista_employee

    @staticmethod
    def getEmployeesByID(id_employee: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee = EmployeeModel()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"SELECT id_dipendente, nome, cognome, cf, iban, tipo_contratto, email, telefono FROM dipendente WHERE id_dipendente = '{id_employee}';")
        record = cursor.fetchone()
        if record is None:
            return employee
        else:
            employee = EmployeeModel(
                id_employee=record[0],
                nome=record[1],
                cognome=record[2],
                cf=record[3],
                iban=record[4],
                tipo_contratto=record[5],
                email=record[6],
                telefono=record[7]
            )
        if connection.is_connected():
            connection.close()

        return employee

    @staticmethod
    def createEmployee(employee: EmployeeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO dipendente(nome, cognome, cf, iban, tipo_contratto, email, telefono) VALUES ('{employee.nome}', '{employee.cognome}', '{employee.cf}', '{employee.iban}', '{employee.tipo_contratto}', '{employee.email}', '{employee.telefono}');")
        connection.commit()
        return employee

    @staticmethod
    def updateEmployeeByID(employee: EmployeeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"UPDATE dipendente SET nome = '{employee.nome}', cognome ='{employee.cognome}', cf = '{employee.cf}', iban ='{employee.iban}', tipo_contratto = '{employee.tipo_contratto}', email ='{employee.email}' , telefono ='{employee.telefono}' WHERE id_dipendente = {employee.id_employee};")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return employee

    @staticmethod
    def deleteEmployeeByID(id_employee: int):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM dipendente WHERE id_dipendente = {id_employee};")
        connection.commit()
        if connection.is_connected():
            connection.close()

    @staticmethod
    def getEmployeeByNameSurname(nome: str, cognome: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        employee = EmployeeModel()
        lista_employee = dict()
        cursor.execute(
            f"SELECT id_dipendente, nome, cognome, cf, iban, tipo_contratto, email, telefono FROM dipendente WHERE nome = '{nome}' AND cognome = '{cognome}';")
        records = cursor.fetchall()
        if records is None:
            return employee
        else:
            for record in records:
                employee = EmployeeModel(
                    id_employee=record[0],
                    nome=record[1],
                    cognome=record[2],
                    cf=record[3],
                    iban=record[4],
                    tipo_contratto=record[5],
                    email=record[6],
                    telefono=record[7]
                )
                lista_employee[record[0]] = employee
        if connection.is_connected():
            connection.close()
        return lista_employee

    @staticmethod
    def getEmployeeBySurname(cognome: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        employee = EmployeeModel()
        lista_employee = dict()
        cursor.execute(
            f"SELECT id_dipendente, nome, cognome, cf, iban, tipo_contratto, email, telefono FROM dipendente WHERE cognome = '{cognome}';")
        records = cursor.fetchall()
        if records is None:
            return employee
        else:
            for record in records:
                employee = EmployeeModel(
                    id_employee=record[0],
                    nome=record[1],
                    cognome=record[2],
                    cf=record[3],
                    iban=record[4],
                    tipo_contratto=record[5],
                    email=record[6],
                    telefono=record[7]
                )
                lista_employee[record[0]] = employee
            if connection.is_connected():
                connection.close()
            return lista_employee

    @staticmethod
    def getEmployeeByCF(cf: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee = EmployeeModel()
        lista = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"SELECT id_dipendente, nome, cognome, cf, iban, tipo_contratto, email, telefono FROM dipendente WHERE cf ='{cf}';")
        record = cursor.fetchone()
        if record is None:
            response = CallBackResponse(esitoChiamata="OK", numeroRisultati=0, error="Codice Fiscale Non Presente")
            lista['response'] = response
        else:
            employee = EmployeeModel(
                id_employee=record[0],
                nome=record[1],
                cognome=record[2],
                cf=record[3],
                iban=record[4],
                tipo_contratto=record[5],
                email=record[6],
                telefono=record[7]
            )
            response = CallBackResponse(esitoChiamata="Ok", numeroRisultati=1)
            lista[record[0]] = employee
            lista['response'] = response
        if connection.is_connected():
            connection.close()
        return lista
        

    @staticmethod
    def getEmployeeByMatricola(matricola: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee = EmployeeModel()
        lista = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"SELECT d.id_dipendente, d.nome,d.cognome,d.cf,d.iban,d.tipo_contratto,d.email,d.telefono from dipendente d join dipendente_azienda da on d.id_dipendente = da.id_dipendente join azienda a on da.id_azienda = a.id_azienda where matricola = '{matricola}'")
        record = cursor.fetchone()
        if record is None:
            response = CallBackResponse(esitoChiamata="OK", numeroRisultati=0, error="Codice Fiscale Non Presente")
            lista['response'] = response
        else:
            employee = EmployeeModel(
                id_employee=record[0],
                nome=record[1],
                cognome=record[2],
                cf=record[3],
                iban=record[4],
                tipo_contratto=record[5],
                email=record[6],
                telefono=record[7]
            )
            response = CallBackResponse(esitoChiamata="Ok", numeroRisultati=1)
            lista[record[0]] = employee
            lista['response'] = response
        if connection.is_connected():
            connection.close()
        return lista
        
