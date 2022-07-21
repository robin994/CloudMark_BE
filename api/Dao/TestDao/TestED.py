import logging

from api.Model import EmployeeModel
from api.Model.EmployeeModel import NewEmployeeModel
from EmployeeDAO import EmployeeDAO


class test_employee_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        
        total = 0
        counter = 0
        
        
        # GETALLEMPLOYEES
        try:
            total += 1
            EmployeeDAO.getAllEmployees()
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao getAllEmployee not passed")
            logging.exception(e)
           
           
        employee_create = NewEmployeeModel(
            first_name="Marco",
            last_name="Rossi",
            cf="MSS1234",
            iban="1111",
            id_contractType=1,
            email="marcorossi@gmail.com",
            phoneNumber="33344445555"
        )
        
         
        # CREATEEMPLOYEE
        try:
            total += 1
            uuidEmployee = EmployeeDAO.createEmployee(employee_create)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao createEmployee not passed")
            logging.exception(e)
          
        # GETEMPLOYEESBYID 
        try:
            total += 1
            EmployeeDAO.getEmployeesByID(uuidEmployee['response'])
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao getEmployeesByID not passed")
            logging.exception(e)
    
        # UPDATEEMPLOYEEBYID   
        try:
            employee_update = EmployeeModel(
                id_employee=uuidEmployee['response'],
                first_name="Giorgino",
                last_name="Giovannino",
                cf="72211",
                iban= "45612",
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
          

        # GETEMPLOYEESBYBUSINESS
        try:
            total += 1
            EmployeeDAO.getEmployeesByBusiness('124e4567-e85b-1fd3-a456-426614474000')
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao getEmployeesByBusiness not passed")
            logging.exception(e)
          
          
        #GETEMPLOYEESBYACCOUNT
        try:
          total += 1
          EmployeeDAO.getEmployeesByAccount('e55917e1-0e9f-40b2-92ae-c880328aa110')
          counter += 1
        except(RuntimeError, TypeError, NameError) as e:
          logging.error("EmployeeDao getEmployeesByAccount not passed")
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
            EmployeeDAO.deleteEmployeeByID(uuidEmployee['response'])
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao deleteEmployeeByID not passed")
            logging.exception(e)
    
          
        # GETEMPLOYEESBYLASTWORK
        try:
            total += 1
            EmployeeDAO.getEmployeesByLastWork()
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("EmployeeDao getEmployeesByLastWork not passed")
            logging.exception(e)
          

        #RESULT SOLVE EMPLOYEE DAO   
        logging.warning("Test EmployeeDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)   
        
            
if __name__=="__main__":
    test_employee_dao.main()
