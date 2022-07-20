import logging
from EmployeeDAO import EmployeeDAO
from Model.EmployeeModel import EmployeeModel
from api.Model.EmployeeModel import NewEmployeeModel

class test_employee_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        
        total = 0
        counter = 0
        
        
        # GETALLEMPLOYEES
        # try:
        #     total += 1
        #     EmployeeDAO.getAllEmployees()
        #     counter += 1
        # except(RuntimeError, TypeError, NameError) as e:
        #     logging.error("EmployeeDao getAllEmployee not passed")
        #     logging.exception(e)
           
           
        # GETEMPLOYEESBYID 
        # try:
        #     total += 1
        #     EmployeeDAO.getEmployeesByID('124e4567-e85b-1fd3-a456-333322233412')
        #     counter += 1
        # except(RuntimeError, TypeError, NameError) as e:
        #     logging.error("EmployeeDao getEmployeesByID not passed")
        #     logging.exception(e)
         
        employee_create = NewEmployeeModel(
            first_name="Marco",
            last_name="Rossi",
            cf="MSS1234",
            iban="1111",
            id_contractType=1,
            email="marcorossi@gmail.com",
            phoneNumber="33344445555"
        )
        
        # employee_create2 = NewEmployeeModel(
        #     first_name="Luca",
        #     last_name="Verdi",
        #     cf="1111",
        #     iban="2222",
        #     id_contractType=1,
        #     email="lucaverdi@gmail.com",
        #     phoneNumber="33344445555"
        # )
           
           
        # CREATEEMPLOYEE
        try:
            total += 1
            uuidEmployee = EmployeeDAO.createEmployee(employee_create)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao createEmployee not passed")
            logging.exception(e)
            
        
        # UPDATEEMPLOYEEBYID   
        try:
            employee_update = EmployeeModel(
                id_employee="124e4567-e85b-1fd3-a456-333322233412",
                first_name="Giorgino",
                last_name="Giovannino",
                cf="72211",
                iban="45612",
                id_contractType=1,
                email="giorgiogiovanni@jojo.snuff",
                phoneNumber="0001112222"
            )
            
            total += 1
            EmployeeDAO.updateEmployeeByID(employee_update)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao updateEmployeeByID not passed")
            logging.exception(e)
       
        # FILTERBYEMPLOYEE
        try:
            total += 1
            EmployeeDAO.filterByEmployee(employee_update, '124e4567-e85b-1fd3-a456-426614474000')
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao filterByEmployee not passed")
            logging.exception(e)
            
        # DELETEEMPLOYEEBYID
        try:
            total += 1
            EmployeeDAO.deleteEmployeeByID(uuidEmployee)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao deleteEmployeeByID not passed")
            logging.exception(e)
        
        

        
        
        # GETEMPLOYEEBYSURNAME
        # try:
        #     total += 1
        #     EmployeeDAO.getEmployeeBySurname('Giovannino')
        #     counter += 1
        # except(RuntimeError, TypeError, NameError) as e:
        #     logging.error("EmployeeDao getEmployeeBySurname not passed")
        #     logging.exception(e)
            
        
        # # GETEMPLOYEEBYCF
        # try:
        #     total += 1
        #     EmployeeDAO.getEmployeeByCF('72211')
        #     counter += 1
        # except(RuntimeError, TypeError, NameError) as e:
        #     logging.error("EmployeeDao getEmployeeByCF not passed")
        #     logging.exception(e)
            
            
        # # GETEMPLOYEEBYMATRICOLA
        # try:
        #     total += 1
        #     EmployeeDAO.getEmployeeByMatricola('000')
        #     counter += 1
        # except(RuntimeError, TypeError, NameError) as e:
        #     logging.error("EmployeeDao getEmployeeByMatricola not passed")
        #     logging.exception(e)
            
            
        # # GETEMPLOYEESBYLASTWORK
        # try:
        #     total += 1
        #     EmployeeDAO.getEmployeesByLastWork()
        #     counter += 1
        # except(RuntimeError, TypeError, NameError) as e:
        #     logging.error("EmployeeDao getEmployeesByLastWork not passed")
        #     logging.exception(e)
            
        logging.warning("Test EmployeeDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)   
        
            
if __name__=="__main__":
    test_employee_dao.main()