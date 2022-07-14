from distutils.errors import CompileError
from API.Model.AccountModel import AccountModel
from AccountDao import AccountDao
from Model.AccountModel import AccountModel
from CustomerDao import CustomerDao
from Model.CustomerModel import CustomerModel
from EmployeeDAO import EmployeeDAO
from Model.EmployeeModel import EmployeeModel
from OrderDAO import CommessaDAO
from Model.OrderModel import OrderModel
# from TipoAccountDao import TipoAccountDao
# from TipoPresenzaDao import TipoPresenzaDao
# from Model.TipoAccount import TipoAccount
# from Model.TipoPresenza import TipoPresenza
import logging

class test:
  def main():
    ###### TEST AccountDAO ######
    # logging.warning(AccountDao.getAllAccounts())
    # account = AccountModel(id_account=3, user="Franco", password='aaaa', abilitato='1', tipo_account='Administrator')
    # logging.warning(AccountDao.getAccountByID(1))
    # logging.warning(AccountDao.createAccount(account))
    # logging.warning(AccountDao.updateAccountByID(account))
    # logging.warning(AccountDao.deleteAccountByID(3))

    ###### TEST CustomerDAO ######
    # logging.warning(CustomerDao.getAllCustomers())
    # customerCreate = CustomerModel(name="Pluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # customerUpdate = CustomerModel(id_customer=2, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # logging.warning(CustomerDao.getCustomerByID(1))
    # logging.warning(CustomerDao.createCustomer(customerCreate))
    # logging.warning(CustomerDao.updateCustomerByID(customerUpdate))
    # logging.warning(CustomerDao.deleteCustomerByID(2))
    
    ###### TEST EmployeeDAO ######
    # logging.warning(EmployeeDAO.getAllEmployees())
    # logging.warning(EmployeeDAO.getEmployeesByID(1))
    # logging.warning(EmployeeDAO.getEmployeeBySurname('rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByNameSurname('mario','rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByCF('123'))
    # employeeCreate = EmployeeModel(nome="Franco", cognome="Baresi", cf="1234", iban="0001", tipo_contratto="indeterminato", email="francobaresimilan@gmail.com", telefono='123456789')
    # employeeUpdate = EmployeeModel(id_employee="2", nome="Franco", cognome="Baresi", cf="1234", iban="0001", tipo_contratto="indeterminato", email="francobaresi6@gmail.com", telefono='123456789')
    # logging.warning(EmployeeDAO.createEmployee(employeeCreate))
    # logging.warning(EmployeeDAO.updateEmployeeByID(employeeUpdate))
    # logging.warning(EmployeeDAO.deleteEmployeeByID(2))
    
    ###### TEST OrderDAO ######
    logging.warning(CommessaDAO.getAllOrders())
    logging.warning(CommessaDAO.getOrderByID(1))
    orderCreate = OrderModel(descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2022-01-03")
    logging.warning(CommessaDAO.createOrder(orderCreate))
    orderUpdate = OrderModel(id_order=2, descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2023-01-03")
    logging.warning(CommessaDAO.updateOrderById(orderUpdate))
    logging.warning(CommessaDAO.deleteOrderByID(2))

    
    # ######  TESTING tipo_account  ######
    
    # logging.warning(TipoAccountDao.getAllTipoAccount())
    # logging.warning(TipoAccountDao.getTipoAccountByNomeTipoAccount("administrator"))
    # tipoAccount = TipoAccount(nomeTipoAccount="provupdate",funzioneProfilo="ciaoo")
    # tipoAccountDaAggiornare = TipoAccount(nomeTipoAccount="provupdate",funzioneProfilo="provaupdate")
    # logging.warning(TipoAccountDao.insertTipoAccount(tipoAccount))
    # logging.warning(TipoAccountDao.deleteTipoAccount("prova"))
    # logging.warning(TipoAccountDao.updateTipoAccount(tipoAccountDaAggiornare))
    
    # ########  TESTING tipo_presenza  ##########
    
    # logging.info("TEST TIPO PRESENZA DAO")
    
    # logging.warning(TipoPresenzaDao.getAllTipoPresenza())
    # logging.warning(TipoPresenzaDao.getTipoPresenzabyNomeTipoPresenza("ASSENZA"))
    # tipoPresenza = TipoPresenza(nomeTipoPresenza="provapresenza",percentualeMaggiorazione= 20,pagaOraria=10)
    # tipoPresenzaDaAggiornare = TipoPresenza(nomeTipoPresenza="aa",percentualeMaggiorazione= 40,pagaOraria=10)
    # logging.warning(TipoPresenzaDao.insertTipoPresenza(tipoPresenza))
    # logging.warning(TipoPresenzaDao.deleteTipoPresenza("provapresenza"))
    # logging.warning(TipoPresenzaDao.updateTipoPresenza(tipoPresenzaDaAggiornare))

    ######## TESTING dipendente #############
    # logging.warning(EmployeeDAO.getEmployeeByID(1))
    # logging.warning(EmployeeDAO.getEmployeeByNameSurname('Bruno', 'Rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByCF('123'))
    # logging.warning(EmployeeDAO.getEmployeeBySurname('Rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByMatricola('0000'))

if __name__ == "__main__":
   test.main()