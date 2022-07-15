from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from Model.EmployeeModel import EmployeeModel
from DB.DBUtility import DBUtility

class EmployeeDAO:
    
    @staticmethod
    def getAllEmployees():
        connection: MySQLConnection = DBUtility.getLocalConnection()
        # lista = ['id_dipendente', 'nome', 'cognome', 'cf', 'iban', 'tipo_contratto', 'email', 'telefono']
        lista = list()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente""")
        records = cursor.fetchall()
        
        # for count in range(8):
        #     # dizionario[lista[count]] = list(records)[count]
        #     print(count)
        
        # if connection.is_connected():
        #     connection.close()
        #     return list(records)
        
        for row in records:
            employee = EmployeeModel(
                id=row[0],
                nome=row[1],
                cognome=row[2],
                cf=row[3],
                iban=row[4],
                tipo_contratto=row[5],
                email=row[6],
                telefono=row[7]
            )
        lista.append(employee)
        if connection.is_connected():
            connection.close()
            return lista
    
    @staticmethod
    def getEmployeesByID(AccountID: int):
        employee = EmployeeModel()
        connection: MySQLConnection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente Where id_dipendente = %s""", (AccountID, ))
        record = cursor.fetchone()
        if record is None:
            return employee
        else:
            employee = EmployeeModel(
                id=record[0],
                # nome=record[1],
                # cognome=[2],
                # cf=record[3],
                # iban=record[4],
                # email=record[5],
                # telefono=record[6]
            )
        if connection.is_connected():
            connection.close()
            return employee

    @staticmethod
    def createEmployee(employee:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dipendente(id_dipendente, nome, cognome, cf, iban, email, telefono, matricola) VALUES(%s, %s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                employee['id'],
                                employee['nome'],
                                employee['cognome'],
                                employee['cf'],
                                employee['iban'],
                                employee['email'],
                                employee['telefono'],
                                employee['matricola']
                        ))
        return cursor.fetchall()

    @staticmethod
    def updateEmployeeByID(employee:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE dipendente SET nome = '%s', cognome ='%s', cf = '%s', iban ='%s' , email ='%s' , telefono ='%s', matricola='%s' where id_dipendente = '%s'; COMMIT;", (
                                employee['nome'],
                                employee['cognome'],
                                employee['cf'],
                                employee['iban'],
                                employee['email'],
                                employee['telefono'],
                                employee['id'],
                                employee['matricola']
                        ))
        return cursor.fetchall()    

    @staticmethod
    def deleteEmployeeByID(id):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM dipendente WHERE id_dipendente =", id)
        return cursor.commit()

    @staticmethod
    def getEmployeeByNameSurname(nome:str, cognome:str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista = list()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente D WHERE D.nome = %s and D.cognome = %s;""", (nome, cognome))
        records = cursor.fetchall()
        for row in records:
            employee = EmployeeModel(
                id=row[0],
                nome=row[1],
                cognome=row[2],
                cf=row[3],
                iban=row[4],
                tipo_contratto=row[5],
                email=row[6],
                telefono=row[7]
        )
        lista.append(employee)
        if connection.is_connected():
            connection.close()
            return lista

    @staticmethod
    def getEmployeeBySurname(cognome:str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista = list()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente D WHERE D.cognome = %s;""", (cognome, ))
        records = cursor.fetchall()
        for row in records:
            employee = EmployeeModel(
                id=row[0],
                nome=row[1],
                cognome=row[2],
                cf=row[3],
                iban=row[4],
                tipo_contratto=row[5],
                email=row[6],
                telefono=row[7]
        )
        lista.append(employee)
        if connection.is_connected():
            connection.close()
            return lista

    @staticmethod
    def getEmployeeByCF(cf:str):
        connection: MySQLConnection = DBUtility.getLocalConnection()
        lista = list()
        cursor = connection.cursor()
        cursor.execute(f"select * from dipendente d where d.cf = '{cf}'")
        record = cursor.fetchone()
        employee = EmployeeModel(
            id=record[0],
            nome=record[1],
            cognome=record[2],
            cf=record[3],
            iban=record[4],
            tipo_contratto=record[5],
            email=record[6],
            telefono=record[7]
        )
        lista.append(employee)
        return lista

    # @staticmethod
    # def getEmployeeByMatricola(matricola:str):
    #     connection: MySQLConnection = DBUtility.getLocalConnection()
    #     lista = list()
    #     cursor = connection.cursor()
    #     cursor.execute("""SELECT * FROM dipendente D WHERE D.matricola = %s;""", (matricola, ))
    #     # testato il funzionamento ricercando nel campo telefono, colonna matricola da aggiungere nel DB
    #     record = cursor.fetchone()
    #     for row in record:
    #         employee = EmployeeModel(
    #             id=row[0],
    #             nome=row[1],
    #             cognome=row[2],
    #             cf=row[3],
    #             iban=row[4],
    #             tipo_contratto=row[5],
    #             email=row[6],
    #             telefono=row[7],
    #         )
    #         lista.append(employee)
    #     if connection.is_connected():
    #         connection.close()
    #         return lista
