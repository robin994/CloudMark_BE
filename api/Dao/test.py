from distutils.errors import CompileError
from API.Model.AccountModel import AccountModel
from AccountDao import AccountDao
from Model.AccountModel import AccountModel
from BusinessDao import BusinessDao
from Model.BusinessModel import BusinessModel
from CustomerDao import CustomerDao
from Model.CustomerModel import CustomerModel
from EmployeeDAO import EmployeeDAO
from Model.EmployeeModel import EmployeeModel
from OrderDAO import CommessaDAO
from Model.OrderModel import OrderModel
from PresenceDao import PresenceDao
from Model.PresenceModel import PresenceModel
from TipoAccountDao import TipoAccountDao
from Model.TipoAccount import TipoAccount
from TipoContrattoDAO import TipoContrattoDAO
from Model.TipoContratto import TipoContratto
from TipoPresenzaDao import TipoPresenzaDao
from Model.TipoPresenza import TipoPresenza
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

    ###### TEST BusinessDao ######
    logging.warning(BusinessDao.getAllBusiness())
    businessCreate = BusinessModel(name="Pluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    businessUpdate = BusinessModel(id_business=2, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    logging.warning(BusinessDao.getBusinessByID(1))
    logging.warning(BusinessDao.createBusiness(businessCreate))
    logging.warning(BusinessDao.updateBusinessById(businessUpdate))
    logging.warning(BusinessDao.deleteBusinessById(2))

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
    # logging.warning(CommessaDAO.getAllOrders())
    # logging.warning(CommessaDAO.getOrderByID(1))
    # orderCreate = OrderModel(descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2022-01-03")
    # logging.warning(CommessaDAO.createOrder(orderCreate))
    # orderUpdate = OrderModel(id_order=2, descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2023-01-03")
    # logging.warning(CommessaDAO.updateOrderById(orderUpdate))
    # logging.warning(CommessaDAO.deleteOrderByID(2))

    ###### TEST PresenceDAO ######     
    # logging.warning(PresenceDao.getAllPresence())
    # logging.warning(PresenceDao.getPresenceByPrimaryKey(1, '2022-01-01', 'festivo'))
    # presenceCreate = PresenceModel(id_employee=1, date_presence='2022-01-02', typeof_presence='assenza', id_order=1, hours=8)
    # logging.warning(PresenceDao.createPresence(presenceCreate))
    # presenceUpdate = PresenceModel(id_employee=1, date_presence='2022-01-02', typeof_presence='malattia', id_order=1, hours=8)
    # logging.warning(PresenceDao.updatePresenceByIDandDate(presenceUpdate))
    # logging.warning(PresenceDao.deletePresenceByPK(1, '2022-01-02', 'malattia'))

    # ######  TEST tipo_accountDao  ######
    # logging.warning(TipoAccountDao.getAllTipoAccount())
    # logging.warning(TipoAccountDao.getTipoAccountByNomeTipoAccount("administrator"))
    # tipoAccountCreate = TipoAccount(nomeTipoAccount="provupdate",funzioneProfilo="ciaoo")
    # tipoAccountUpdate = TipoAccount(nomeTipoAccount="provupdate",funzioneProfilo="provaupdate")
    # logging.warning(TipoAccountDao.createTipoAccount(tipoAccountCreate))
    # logging.warning(TipoAccountDao.updateTipoAccount(tipoAccountUpdate))
    # logging.warning(TipoAccountDao.deleteTipoAccount("provupdate"))
    
    ###### TEST TipoContrattoDAO ######
    # logging.warning(TipoContrattoDAO.getAllTipoContratto())
    # logging.warning(TipoContrattoDAO.getTipoContrattoByID('indeterminato'))
    # contrattoCreate = TipoContratto(name='determinato', info='txt')
    # contrattoUpdate = TipoContratto(name='determinato', info='text')
    # logging.warning(TipoContrattoDAO.createTipoContratto(contrattoCreate))
    # logging.warning(TipoContrattoDAO.updateTipoContrattoById(contrattoUpdate))
    # logging.warning(TipoContrattoDAO.deleteTipoContrattoById('determinato'))

    # ########  TESTING tipo_presenza  ##########    
    # logging.warning(TipoPresenzaDao.getAllTipoPresenza())
    # logging.warning(TipoPresenzaDao.getTipoPresenzabyNomeTipoPresenza("ASSENZA"))
    # tipoPresenza = TipoPresenza(nomeTipoPresenza="provapresenza",percentualeMaggiorazione= 20,pagaOraria=10)
    # logging.warning(TipoPresenzaDao.insertTipoPresenza(tipoPresenza))
    # tipoPresenzaDaAggiornare = TipoPresenza(nomeTipoPresenza="provapresenza",percentualeMaggiorazione= 40,pagaOraria=10)
    # logging.warning(TipoPresenzaDao.updateTipoPresenza(tipoPresenzaDaAggiornare))
    # logging.warning(TipoPresenzaDao.deleteTipoPresenza("provapresenza"))

if __name__ == "__main__":
   test.main()