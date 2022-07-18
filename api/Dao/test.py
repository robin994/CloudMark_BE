from uuid import uuid4
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
    # ###### TEST AccountDAO ######
    # # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(AccountDao.getAllAccounts())
    # accountCreate = AccountModel(user="Franco", password='aaaa', abilitato='1', id_tipoAccount=1)
    # logging.warning(AccountDao.getAccountByID(1))
    # logging.warning(AccountDao.createAccount(accountCreate))
    # accountUpdate = AccountModel(id_account=2, user="Beppe", password='aaaa', abilitato='1', id_tipoAccount=1)
    # logging.warning(AccountDao.updateAccountByID(accountUpdate))
    # logging.warning(AccountDao.deleteAccountByID(2))

    # # ###### TEST BusinessDao ######
    # # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(BusinessDao.getAllBusiness())
    # businessCreate = BusinessModel(name="Pluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # businessUpdate = BusinessModel(id_business=2, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # logging.warning(BusinessDao.getBusinessByID(1))
    # logging.warning(BusinessDao.createBusiness(businessCreate))
    # logging.warning(BusinessDao.updateBusinessById(businessUpdate))
    # logging.warning(BusinessDao.deleteBusinessById(4))

    # ###### TEST CustomerDAO ######
    # in console mi aspetto 6 warning, il primo mi ritorna il record con tutti i record presenti nella table, il secondo mi ritorna il record con ID=1, il terzo mi torna l'oggetto che ho inserito nella table, il quarto mi torna i clienti corrispondenti all'azienda di ID=1, il quinto mi torna l'oggetto modificato nella table, l'ultimo mi dà la conferma di eliminazione del record
    logging.warning(CustomerDao.getAllCustomers())
    customerCreate = CustomerModel(id_customer=uuid4(), name='pluto', p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    customerUpdate = CustomerModel(id_customer=customerCreate.id_customer, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    logging.warning(CustomerDao.createCustomer(customerCreate))
    # logging.warning(CustomerDao.getCustomerByID(customerCreate.id_customer))
    # logging.warning(CustomerDao.getCustomerByBusinessID('errore'))
    logging.warning(CustomerDao.updateCustomerByID(customerUpdate))
    # logging.warning(CustomerDao.deleteCustomerByID(2))
    
    # # ###### TEST EmployeeDAO ######
    # # in console mi aspetto 9 record. Il primo torna tutti i record della tabella, il secondo il record con ID=1, il terzo ritorna il record con cognome = rossi, il quarto il record con nome = mario && cognome = rossi, il quinto il record con CF = 123, il sesto ritorna il record inserito nella table, il settimo il record aggiornato, l'ottavo conferma l'eliminazione del dipendente con ID = 2, il nono ritorna la lista dei dipendenti in forze all'azienda
    # logging.warning(EmployeeDAO.getAllEmployees())
    # logging.warning(EmployeeDAO.getEmployeesByID(1))
    # logging.warning(EmployeeDAO.getEmployeeBySurname('rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByNameSurname('mario','rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByCF('123'))
    # employeeCreate = EmployeeModel(nome="Franco", cognome="Baresi", cf="1234", iban="0001", id_tipoContratto=1, email="francobaresimilan@gmail.com", telefono='123456789')
    # employeeUpdate = EmployeeModel(id_employee="2", nome="Beppe", cognome="Baresi", cf="1234", iban="0001", id_tipoContratto=1, email="francobaresi6@gmail.com", telefono='123456789')
    # logging.warning(EmployeeDAO.createEmployee(employeeCreate))
    # logging.warning(EmployeeDAO.updateEmployeeByID(employeeUpdate))
    # logging.warning(EmployeeDAO.deleteEmployeeByID(2))
    # logging.warning(EmployeeDAO.getEmployeesByLastWork())

    # # ###### TEST CommessaDAO ######
    # # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(CommessaDAO.getAllOrders())
    # logging.warning(CommessaDAO.getOrderByID(1))
    # commessaCreate = CommessaModel(descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2022-01-03")
    # logging.warning(CommessaDAO.createOrder(commessaCreate))
    # commessaUpdate = CommessaModel(id_order=2, descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2023-01-03")
    # logging.warning(CommessaDAO.updateOrderById(commessaUpdate))
    # logging.warning(CommessaDAO.deleteOrderByID(2))

    # # ###### TEST PresenceDAO ######     
    # # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(PresenceDao.getAllPresence())
    # logging.warning(PresenceDao.getPresenceByPrimaryKey(1, '2022-01-01', 3))
    # presenceCreate = PresenceModel(id_employee=1, date_presence='2022-01-03', id_tipoPresenza=3, id_order=1, hours=8)
    # logging.warning(PresenceDao.createPresence(presenceCreate))
    # presenceUpdate = PresenceModel(id_employee=1, date_presence='2022-01-03', id_tipoPresenza=1, id_order=1, hours=8)
    # logging.warning(PresenceDao.updatePresenceByIDEmployeeAndDate(presenceUpdate))
    # logging.warning(PresenceDao.deletePresenceByPK(1, '2022-01-03', 1))

    # # ######  TEST tipo_accountDao  ######
    # # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(TipoAccountDao.getAllTipoAccount())
    # logging.warning(TipoAccountDao.getTipoAccountByIdTipoAccount(1))
    # tipoAccountCreate = TipoAccount(nomeTipoAccount="provupdate",funzioneProfilo="ciaoo")
    # tipoAccountUpdate = TipoAccount(id_tipoAccount=3, nomeTipoAccount="provupdate",funzioneProfilo="provaupdate")
    # logging.warning(TipoAccountDao.createTipoAccount(tipoAccountCreate))
    # logging.warning(TipoAccountDao.updateTipoAccount(tipoAccountUpdate))
    # logging.warning(TipoAccountDao.deleteTipoAccount(3))
    
    # # ###### TEST TipoContrattoDAO ######
    #  # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.warning(TipoContrattoDAO.getAllTipoContratto())
    # logging.warning(TipoContrattoDAO.getTipoContrattoByID(1))
    # contrattoCreate = TipoContratto(name='determinato', info='txt')
    # contrattoUpdate = TipoContratto(id_tipoContratto=2, name='determinato', info='text')
    # logging.warning(TipoContrattoDAO.createTipoContratto(contrattoCreate))
    # logging.warning(TipoContrattoDAO.updateTipoContrattoById(contrattoUpdate))
    # logging.warning(TipoContrattoDAO.deleteTipoContrattoById(2))

    # # ########  TESTING tipoPresenzaDAO  ########## 
    # #  # in console mi aspetto 5 warning, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2   
    # logging.warning(TipoPresenzaDao.getAllTipoPresenza())
    # logging.warning(TipoPresenzaDao.getTipoPresenzabyIdTipoPresenza(1))
    # tipoPresenza = TipoPresenza(nomeTipoPresenza="provapresenza",percentualeMaggiorazione= 20,pagaOraria=10)
    # logging.warning(TipoPresenzaDao.createTipoPresenza(tipoPresenza))
    # tipoPresenzaDaAggiornare = TipoPresenza(id_tipoPresenza=5, nomeTipoPresenza="provapresenza",percentualeMaggiorazione= 40,pagaOraria=10)
    # logging.warning(TipoPresenzaDao.updateTipoPresenza(tipoPresenzaDaAggiornare))
    # logging.warning(TipoPresenzaDao.deleteTipoPresenza(5))

if __name__ == "__main__":
   test.main()