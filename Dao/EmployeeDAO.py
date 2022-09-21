import logging
from ast import Call
from uuid import UUID, uuid4

from DB.DBUtility import DBUtility
from Model.AccountModel import AccountModel
from Model.BusinessModel import BusinessStartEnd
from Model.EmployeeModel import (AccountEmployeeBusiness, AccountEmployeeModel, EmlpoyeeOrderModel, EmployeeModel,
                                 NewAccountEmployeeModel, NewEmployeeModel, EmployeeBusinessModel)
from Model.LastWorkModel import LastWorkModel
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from Dao.AccountDao import AccountDao
from Dao.CallBackResponse import CallBackResponse

# testati e funzionanti


class EmployeeDAO:

    @staticmethod
    def getAllEmployees():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_employee = dict()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono FROM dipendente")
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
        return CallBackResponse.success(lista_employee)

    @staticmethod
    def getAllEmployeesByEmptyKey():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista_employee = list()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono FROM dipendente")
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
            lista_employee.append(employee)
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(lista_employee)

    @staticmethod
    def getEmployeesByID(id_employee):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        employee = {}
        employee_by_id = {}
        sql = "SELECT * FROM dipendente WHERE id_dipendente = %s;"
        val = (str(id_employee),)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        if record is not None:
            employee = {
                "id_employee": record[0],
                "first_name": record[1],
                "last_name": record[2],
                "cf": record[3],
                "iban": record[4],
                "id_contractType": record[5],
                "email": record[6],
                "phoneNumber": record[7]
            }
            employee_by_id[employee["id_employee"]] = employee
        if connection.is_connected():
            connection.close()
        logging.debug(employee)
        return CallBackResponse.success(employee_by_id)

    @staticmethod
    def createEmployee(employee: NewEmployeeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        uuid = uuid4()
        cursor.execute(
            f"INSERT INTO dipendente(id_dipendente,nome, cognome, cf, iban, id_tipo_contratto, email, telefono) VALUES ('{uuid}','{employee.first_name}', '{employee.last_name}', '{employee.cf}', '{employee.iban}', '{employee.id_contractType}', '{employee.email}', '{employee.phoneNumber}');")
        connection.commit()
        return CallBackResponse.success(uuid)

    @staticmethod
    def updateEmployeeByID(employee: EmployeeModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        update_employee = dict()
        cursor: MySQLCursor = connection.cursor()
        sql = """UPDATE dipendente
                SET nome=%s, cognome=%s, cf=%s, iban=%s, id_tipo_contratto=%s, email=%s, telefono=%s
                WHERE id_dipendente=%s;"""
        val = (employee.first_name, employee.last_name, employee.cf, employee.iban,
               employee.id_contractType, employee.email, employee.phoneNumber, employee.id_employee)
        cursor.execute(sql, val)
        connection.commit()
        update_employee[employee.id_employee] = employee
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(update_employee)

    @staticmethod
    def deleteEmployeeByID(id_employee: UUID):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM dipendente WHERE id_dipendente = '{id_employee}'")
        connection.commit()
        if connection.is_connected():
            connection.close()

        return CallBackResponse.success(id_employee)

    @staticmethod
    def filterByEmployee(emp: NewEmployeeModel, idAzienda: str):
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
            CallBackResponse.bad_request()
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
        return CallBackResponse.success(lista_employee)

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
        return CallBackResponse.success(all_last_work)

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
            CallBackResponse.bad_request()
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
        return CallBackResponse.success(employee_business)

    @staticmethod
    def getEmployeesByAccount(id_account):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee_account = dict()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT *
                FROM dipendente d
                JOIN account_dipendente ad ON d.id_dipendente = ad.id_dipendente
                JOIN account a on a.id_account = ad.id_account
                JOIN dipendente_azienda da on da.id_dipendente = d.id_dipendente
                where a.id_account =%s;"""
        val = (id_account,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        if connection.is_connected():
            connection.close()
        if record is None:
            return CallBackResponse.bad_request()
        else:
            employee = EmployeeModel(
                id_employee=record[0],
                first_name=record[1],
                last_name=record[2],
                cf=record[3],
                iban=record[4],
                id_contractType=record[5],
                email=record[6],
                phoneNumber=record[7],
            )
            account = AccountModel(
                id_account=record[10],
                user=record[11],
                password='',
                abilitato=record[13],
                id_tipo_account=record[14],
            )
            response = AccountEmployeeModel(
                employee=employee,
                account=account,
                id_business=record[16],
                start_date=record[17],
                serial_num=record[18],
                end_date=record[19],)
        return CallBackResponse.success(response)

    @staticmethod
    def createNewAccountEmployee(payload: NewAccountEmployeeModel):
        res_acc = AccountDao.createAccount(payload.new_account)
        res_emp = EmployeeDAO.createEmployee(payload.new_employee)
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """INSERT INTO account_dipendente (id_account, id_dipendente) VALUES(%s, %s)"""
        val = (str(res_acc.data), str(res_emp.data))
        cursor.execute(sql, val)
        sql = """INSERT INTO dipendente_azienda (id_dipendente, id_azienda, data_inizio_rapporto, matricola, data_fine_rapporto) VALUES(%s, %s,%s,%s,%s)"""
        val = (str(res_emp.data), payload.id_business,
               payload.start_date, payload.serial_num, payload.end_date)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(res_emp)

    @staticmethod
    def getAllEmployeesAccountBusiness(id_business : str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        employee_account_business = dict()
        cursor: MySQLCursor = connection.cursor()
        sql = """SELECT *
                FROM dipendente d
                JOIN account_dipendente ad ON d.id_dipendente = ad.id_dipendente
                JOIN account a on a.id_account = ad.id_account
                JOIN dipendente_azienda da on da.id_dipendente = d.id_dipendente
                WHERE da.id_azienda = %s;"""
        val = (id_business,)
        cursor.execute(sql,val,)
        records = cursor.fetchall()
        if connection.is_connected():
            connection.close()
        if records is None:
            return CallBackResponse.bad_request()
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
                account = AccountModel(
                    id_account=record[10],
                    user=record[11],
                    password='',
                    abilitato=record[13],
                    id_tipo_account=record[14]
                )
                business = BusinessStartEnd(
                    id_business=record[16],
                    start_date=record[17],
                    serial_num=record[18],
                    end_date=record[19]
                )
                employee_account_business[record[0]] = AccountEmployeeBusiness(employee=employee, account=account, business=business)
        return CallBackResponse.success(employee_account_business)

    @staticmethod
    def disableAccountByEmployeeID(id_employee: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql1 = """SELECT A.id_account FROM dipendente D, account_dipendente AD, account A WHERE A.id_account = AD.id_account AND AD.id_dipendente = D.id_dipendente AND D.id_dipendente = %s;"""
        val1 = (id_employee, )
        cursor.execute(sql1, val1)
        id_account = cursor.fetchone()
        if id_account is None:
            return CallBackResponse.bad_request('Nessun account è associato a questo dipendente.')
        else:    
            sql2 = """UPDATE account SET abilitato = 0 WHERE id_account = %s;"""
            val2 = (str(id_account[0]), )
            cursor.execute(sql2, val2)
            connection.commit()
        
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success('OK', description="Account disabilitato con successo.")

    @staticmethod
    def enableAccountByEmployeeID(id_employee: str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql1 = """SELECT A.id_account FROM dipendente D, account_dipendente AD, account A WHERE A.id_account = AD.id_account AND AD.id_dipendente = D.id_dipendente AND D.id_dipendente = %s;"""
        val1 = (id_employee, )
        cursor.execute(sql1, val1)
        id_account = cursor.fetchone()
        if id_account is None:
            return CallBackResponse.bad_request('Nessun account è associato a questo dipendente.')
        else:    
            sql2 = """UPDATE account SET abilitato = 1 WHERE id_account = %s;"""
            val2 = (str(id_account[0]), )
            cursor.execute(sql2, val2)
            connection.commit()
        
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success('OK', description="Account abilitato con successo.")
    
    @staticmethod
    def getEmployeeByIdOrder(id_order : str):
        connection : MySQLConnection = DBUtility.getLocalConnection()
        lista = list()
        cursor : MySQLCursor = connection.cursor()
        sql = """ select d.id_dipendente, d.nome, d.cognome,d.cf,d.email,d.telefono,c.id_commessa from dipendente d join commessa_dipendente cd on d.id_dipendente = cd.id_dipendente join commessa c on cd.id_commessa = c.id_commessa where c.id_commessa = %s"""
        val = (id_order,)
        cursor.execute(sql,val,)
        records = cursor.fetchall()
        for row in records:
            employee = EmlpoyeeOrderModel(
                id_employee = row[0],
                first_name = row[1],
                last_name = row[2],
                cf = row[3],
                email=row[4],
                phone_number=row[5],
                id_order = row[6]
            )
            lista.append(employee)
        if connection.is_connected():
            connection.close()
        return CallBackResponse.success(lista)

    @staticmethod
    def insertEmployeeIntoBusiness(payload: EmployeeBusinessModel):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        sql = """INSERT INTO dipendente_azienda VALUES (%s, %s, %s, %s, %s);"""
        val = (payload.id_employee, payload.id_business, payload.start_date, payload.serial_num, payload.end_date)
        cursor.execute(sql, val)
        connection.commit()
        if connection.is_connected():
            connection.close()
            
        return CallBackResponse.success(payload)
    @staticmethod
    def checkAccountByEmployee(id_dipendente: str):
        """ Check if given employee id is related to an account id """
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            """ SELECT id_account FROM account_dipendente
                WHERE id_dipendente=%s """, 
            (id_dipendente,)
            )
        rows = cursor.fetchall()
        if not rows:
            return {"ok": "not"}
        return {"ok": "ok"}
