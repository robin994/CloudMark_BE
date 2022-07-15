from xml.dom.minicompat import EmptyNodeList
from AccountDao import AccountDao
from Model.AccountModel import AccountModel
from BusinessDao import BusinessDao
from Model.BusinessModel import BusinessModel
from CustomerDao import CustomerDao
from Model.CustomerModel import CustomerModel
from EmployeeDAO import EmployeeDAO
from Model.EmployeeModel import EmployeeModel
from CommessaDAO import CommessaDAO
from Model.CommessaModel import CommessaModel
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
    # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(AccountDao.getAllAccounts())
    # accountCreate = AccountModel(user="Franco", password='aaaa', abilitato='1', tipo_account='Administrator')
    # logging.warning(AccountDao.getAccountByID(1))
    # logging.warning(AccountDao.createAccount(accountCreate))
    # accountUpdate = AccountModel(id_account=2, user="Beppe", password='aaaa', abilitato='1', tipo_account='Administrator')
    # logging.warning(AccountDao.updateAccountByID(accountUpdate))
    # logging.warning(AccountDao.deleteAccountByID(2))

    # ###### TEST BusinessDao ######
    # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(BusinessDao.getAllBusiness())
    # businessCreate = BusinessModel(name="Pluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # businessUpdate = BusinessModel(id_business=2, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # logging.warning(BusinessDao.getBusinessByID(1))
    # logging.warning(BusinessDao.createBusiness(businessCreate))
    # logging.warning(BusinessDao.updateBusinessById(businessUpdate))
    # logging.warning(BusinessDao.deleteBusinessById(4))

    # ###### TEST CustomerDAO ######
    # logging.warning(CustomerDao.getAllCustomers())
    # customerCreate = CustomerModel(name="Pluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # customerUpdate = CustomerModel(id_customer=2, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # logging.warning(CustomerDao.getCustomerByID(1))
    # logging.warning(CustomerDao.createCustomer(customerCreate))
    # logging.warning(CustomerDao.updateCustomerByID(customerUpdate))
    # logging.warning(CustomerDao.deleteCustomerByID(2))
    
    # ###### TEST EmployeeDAO ######
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
    # logging.warning(EmployeeDAO.getEmployeesByLastWork())

    # ###### TEST CommessaDAO ######
    # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    logging.warning(CommessaDAO.getAllOrders())
    logging.warning(CommessaDAO.getOrderByID(1))
    commessaCreate = CommessaModel(descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2022-01-03")
    logging.warning(CommessaDAO.createOrder(commessaCreate))
    commessaUpdate = CommessaModel(id_order=2, descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2023-01-03")
    logging.warning(CommessaDAO.updateOrderById(commessaUpdate))
    logging.warning(CommessaDAO.deleteOrderByID(2))
    

    # ###### TEST PresenceDAO ######     
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
    
    # ###### TEST TipoContrattoDAO ######
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