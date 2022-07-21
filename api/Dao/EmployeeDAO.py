from uuid import UUID, uuid4

from DB.DBUtility import DBUtility
from Model.EmployeeModel import EmployeeModel, NewEmployeeModel
from Model.LastWorkModel import LastWorkModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

# testati e funzionanti


class EmployeeDAO:

    @staticmethod
    def getAllEmployees():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_employee = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute("SELECT id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono FROM dipendente")
        records = cursor.fetchall()
        for row in records:
            employee = EmployeeModel(
                id_employee=row[0],
                first_name=row[1],
                last_name=row[2],
                cf=row[3],
                iban=row[4],
                id_contractType=row[5],
                email=row[6],
                phoneNumber=row[7]
            )
            lista_employee[row[0]] = employee
        if connection.is_connected():
            connection.close()
        return lista_employee

    @staticmethod
    def getEmployeesByID(id_employee: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee = NewEmployeeModel()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute("""SELECT id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono FROM dipendente WHERE id_dipendente = '{id_employee}';""")
        record = cursor.fetchone()
        if record is None:
            return employee
        else:
            employee = NewEmployeeModel(
                id_employee=record[0],
                first_name=record[1],
                last_name=record[2],
                cf=record[3],
                iban=record[4],
                id_contractType=record[5],
                email=record[6],
                phoneNumber=record[7]
            )
        if connection.is_connected():
            connection.close()
        print(employee)
        return employee
    
    @staticmethod
    def createEmployee(employee: NewEmployeeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        uuid = uuid4()
        cursor.execute(
            f"INSERT INTO dipendente(id_dipendente,nome, cognome, cf, iban, id_tipo_contratto, email, telefono) VALUES ('{uuid}','{employee.first_name}', '{employee.last_name}', '{employee.cf}', '{employee.iban}', '{employee.id_contractType}', '{employee.email}', '{employee.phoneNumber}');")
        connection.commit()
        return {'response':uuid}

    @staticmethod
    def updateEmployeeByID(employee: EmployeeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """UPDATE dipendente 
                SET nome=%s, cognome=%s, cf=%s, iban=%s, id_tipo_contratto=%s, email=%s, telefono=%s
                WHERE id_dipendente=%s;"""
        val = (employee.first_name, employee.last_name, employee.cf, employee.iban, employee.id_contractType, employee.email, employee.phoneNumber, employee.id_employee)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return employee

    @staticmethod
    def deleteEmployeeByID(id_employee: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM dipendente WHERE id_dipendente = '{id_employee}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

    @staticmethod
    def filterByEmployee(emp: EmployeeModel, idAzienda: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        lista_employee = dict()
        sql = """SELECT * FROM dipendente
        JOIN dipendente_azienda ON dipendente.id_dipendente = dipendente_azienda.id_dipendente  
        WHERE `id_azienda` = %s AND  `nome` LIKE %s AND `cognome` LIKE %s AND `cf` LIKE %s 
        AND `iban` LIKE %s AND `email` LIKE %s AND `telefono` LIKE %s"""
        val = (idAzienda, '%'+emp.first_name+'%', '%'+emp.last_name+'%', '%'+emp.cf +
               '%', '%'+emp.iban+'%', '%'+emp.email+'%', '%'+emp.phoneNumber+'%',)
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if records is None:
            return ''
        else:
            for record in records:
                employee = EmployeeModel(
                    id_employee=record[0],
                    first_name=record[1],
                    last_name=record[2],
                    cf=record[3],
                    iban=record[4],
                    id_contractType=record[5],
                    email=record[6],
                    phoneNumber=record[7]
                )
                lista_employee[record[0]] = employee
        if connection.is_connected():
            connection.close()
        return lista_employee

    @staticmethod
    def getEmployeesByLastWork():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        all_last_work = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            """SELECT dipendente.cognome, dipendente.nome, dipendente_azienda.matricola, dipendente.cf, dipendente_azienda.data_inizio_rapporto 
            FROM dipendente 
            INNER JOIN dipendente_azienda 
            ON dipendente_azienda.data_fine_rapporto IS NOT NULL""")
        records = cursor.fetchall()

        for record in records:
            last_work = LastWorkModel(
                name=record[0],
                cognome=record[1],
                matricola=record[2],
                cf=record[3],
                data_assunzione=record[4]
            )
            all_last_work[f"{record[0]}_{record[1]}"] = last_work
        if connection.is_connected():
            connection.close()
        return all_last_work
    
    @staticmethod
    def getEmployeesByBusiness(id_business):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee_business = dict()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT d.id_dipendente, d.nome, d.cognome, d.cf, d.iban, d.id_tipo_contratto, d.email, d.telefono 
                FROM dipendente d, azienda a, dipendente_azienda da 
                WHERE d.id_dipendente = da.id_dipendente AND da.id_azienda = a.id_azienda AND a.id_azienda = %s"""
        val = ([id_business])
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if connection.is_connected():
                connection.close()
        if records is None:
            return {}
        else:
            for row in records:
                employee = EmployeeModel(
                    id_employee=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    cf=row[3],
                    iban=row[4],
                    id_contractType=row[5],
                    email=row[6],
                    phoneNumber=row[7]
                )
                employee_business[row[0]] = employee
        return employee_business
    
    @staticmethod
    def getEmployeesByAccount(id_account):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee_account = dict()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT d.id_dipendente, d.nome, d.cognome, d.cf, d.iban, d.id_tipo_contratto, d.email, d.telefono 
                FROM dipendente d, account a, account_dipendente ad 
                WHERE d.id_dipendente = ad.id_dipendente AND ad.id_account = a.id_account AND a.id_account = %s"""
        val = ([id_account])
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if connection.is_connected():
                connection.close()
        if records is None:
            return {}
        else:
            for row in records:
                employee = EmployeeModel(
                    id_employee=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    cf=row[3],
                    iban=row[4],
                    id_contractType=row[5],
                    email=row[6],
                    phoneNumber=row[7]
                )
                employee_account[row[0]] = employee
        print(employee_account)
        return employee_account
