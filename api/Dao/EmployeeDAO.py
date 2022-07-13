from Model.EmployeeModel import EmployeeModel
from DB.DBUtility import DBUtility

class EmployeeDAO:

    @staticmethod
    def getAllEmployees():
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente""")
        return cursor.fetchall()
    
    @staticmethod
    def getEmployeesByID(AccountID):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dipendente Where id_dipendente = ", AccountID)
        return cursor.fetchone()

    @staticmethod
    def createEmployee(employee:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dipendente(id_dipendente, nome, cognome, cf, iban, email, telefono,) VALUES(%s, %s, %s, %s, %s, %s, %s); COMMIT;", (
                                employee['id'],
                                employee['nome'],
                                employee['cognome'],
                                employee['cf'],
                                employee['iban'],
                                employee['email'],
                                employee['telefono']
                        ))
        return cursor.fetchall()

    @staticmethod
    def updateEmployeeByID(employee:EmployeeModel):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE dipendente SET nome = '%s', cognome ='%s', cf = '%s', iban ='%s' , email ='%s' , telefono ='%s' where id_dipendente = '%s'; COMMIT;", (
                                employee['nome'],
                                employee['cognome'],
                                employee['cf'],
                                employee['iban'],
                                employee['email'],
                                employee['telefono'],
                                employee['id']
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
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente D WHERE D.nome = %s and D.cognome = %s;""", (nome, cognome))
        return cursor.fetchall()

    @staticmethod
    def getEmployeeBySurname(cognome:str):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente D WHERE D.cognome = %s;""", (cognome, ))
        return cursor.fetchall()

    @staticmethod
    def getEmployeeByCF(cf:str):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente D WHERE D.cf = %s""", (cf, ))
        return cursor.fetchone()

    @staticmethod
    def getEmployeeByMatricola(matricola:str):
        connection = DBUtility.getLocalConnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM dipendente D WHERE D.telefono = %s;""", (matricola, ))
        return cursor.fetchone()
