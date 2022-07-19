import logging
from unicodedata import name
from uuid import uuid4
from api.Dao.TestDao.TestAD import test_account_dao
from api.Dao.TestDao.TestBD import test_business_dao


class test:
  def main():
    
    logging_level = logging.WARNING
    test_account_dao.main(logging_level)
    #test_business_dao.main(logging_level)

    # ###### TEST BusinessDao ######
    # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.info(BusinessDao.getAllBusiness())
    # businessCreate = BusinessModel(name="Pluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # businessUpdate = BusinessModel(id_business=2, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # logging.info(BusinessDao.getBusinessByID(1))
    # logging.info(BusinessDao.createBusiness(businessCreate))
    # logging.info(BusinessDao.updateBusinessById(businessUpdate))
    # logging.info(BusinessDao.deleteBusinessById(4))
# 
    # ###### TEST CustomerDAO ######
    # in console mi aspetto 6 info, il primo mi ritorna il record con tutti i record presenti nella table, il secondo mi ritorna il record con ID=1, il terzo mi torna l'oggetto che ho inserito nella table, il quarto mi torna i clienti corrispondenti all'azienda di ID=1, il quinto mi torna l'oggetto modificato nella table, l'ultimo mi dà la conferma di eliminazione del record
    # gging.info(CustomerDao.getAllCustomers())
    # stomerCreate = CustomerModel(id_customer=uuid4(), name='pluto', p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # stomerUpdate = CustomerModel(id_customer=customerCreate.id_customer, name="notPluto", p_iva="aaabbbcccee", address="Via Sfarulli, 8", cap="01100", iban="IT94L0355555555555555555553", phone="06222222222", email="grossaaziendapluto@gmail.com", pec="pluto@pec.it", fax="06222222222")
    # gging.info(CustomerDao.createCustomer(customerCreate))
    # logging.info(CustomerDao.getCustomerByID(customerCreate.id_customer))
    # logging.info(CustomerDao.getCustomerByBusinessID('errore'))
    # gging.info(CustomerDao.updateCustomerByID(customerUpdate))
    # logging.info(CustomerDao.deleteCustomerByID(2))
    #   # ###### TEST EmployeeDAO ######
    # # in console mi aspetto 9 record. Il primo torna tutti i record della tabella, il secondo il record con ID=1, il terzo ritorna il record con cognome = rossi, il quarto il record con nome = mario && cognome = rossi, il quinto il record con CF = 123, il sesto ritorna il record inserito nella table, il settimo il record aggiornato, l'ottavo conferma l'eliminazione del dipendente con ID = 2, il nono ritorna la lista dei dipendenti in forze all'azienda
    # logging.info(EmployeeDAO.getAllEmployees())
    # logging.info(EmployeeDAO.getEmployeesByID(1))
    # logging.info(EmployeeDAO.getEmployeeBySurname('rossi'))
    # logging.info(EmployeeDAO.getEmployeeByNameSurname('mario','rossi'))
    # logging.info(EmployeeDAO.getEmployeeByCF('123'))
    # employeeCreate = NewEmployeeModel(nome="Franco", cognome="Baresi", cf="1234", iban="0001", id_tipoContratto=1, email="francobaresimilan@gmail.com", telefono='123456789')
    # employeeUpdate = EmployeeModel(id_employee="2", nome="Beppe", cognome="Baresi", cf="1234", iban="0001", id_tipoContratto=1, email="francobaresi6@gmail.com", telefono='123456789')
    # logging.info(EmployeeDAO.createEmployee(employeeCreate))
    # logging.info(EmployeeDAO.updateEmployeeByID(employeeUpdate))
    # logging.info(EmployeeDAO.deleteEmployeeByID(2))
    # logging.info(EmployeeDAO.getEmployeesByLastWork())
# 
    # # ###### TEST OrderDao ######
    # # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.info(OrderDao.getAllOrders())
    # logging.info(OrderDao.getOrderByID(1))
    # commessaCreate = CommessaModel(descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2022-01-03")
    # logging.info(OrderDao.createOrder(commessaCreate))
    # commessaUpdate = CommessaModel(id_order=2, descrizione="txt", id_cliente=1, id_azienda=1, data_inizio="2022-01-01", data_fine="2023-01-03")
    # logging.info(OrderDao.updateOrderById(commessaUpdate))
    # logging.info(OrderDao.deleteOrderByID(2))
# 
    # # ###### TEST PresenceDAO ######     
    # # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.info(PresenceDao.getAllPresence())
    # logging.info(PresenceDao.getPresenceByPrimaryKey(1, '2022-01-01', 3))
    # presenceCreate = PresenceModel(id_employee=1, date_presence='2022-01-03', id_tipoPresenza=3, id_order=1, hours=8)
    # logging.info(PresenceDao.createPresence(presenceCreate))
    # presenceUpdate = PresenceModel(id_employee=1, date_presence='2022-01-03', id_tipoPresenza=1, id_order=1, hours=8)
    # logging.info(PresenceDao.updatePresenceByIDEmployeeAndDate(presenceUpdate))
    # logging.info(PresenceDao.deletePresenceByPK(1, '2022-01-03', 1))
# 
    # ######  TEST PresenceTypeDao  ######
    # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.info(AccountTypeDao.getAllAccountsType())
    # logging.info(AccountTypeDao.getAccountTypeById(1))
    # tipoAccountCreate = AccountType(name="provupdate",function="ciaoo")
    # tipoAccountUpdate = AccountType(id_tipoAccount=3, name="provupdate",function="provaupdate")
    # logging.info(AccountTypeDao.createAccountType(tipoAccountCreate))
    # logging.info(AccountTypeDao.updateAccountType(tipoAccountUpdate))
    # logging.info(AccountTypeDao.deleteAccountType(3))
    #   # ###### TEST TipoContrattoDAO ######
    #  # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    # logging.info(ContractTypeDAO.getAllContractsType())
    # logging.info(ContractTypeDAO.getContractTypeByID(1))
    # contrattoCreate = ContractType(name='determinato', info='txt')
    # contrattoUpdate = ContractType(id_contractType=2, name='determinato', info='text')
    # logging.info(ContractTypeDAO.createContractType(contrattoCreate))
    # logging.info(ContractTypeDAO.updateContractTypeById(contrattoUpdate))
    # logging.info(ContractTypeDAO.deleteContractTypeById(2))

    # ########  TESTING tipoPresenzaDAO  ########## 
    #  # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2   
    # logging.info(PresenceTypeDao.getAllPresenceType())
    # logging.info(PresenceTypeDao.getPresenceTypebyId(1))
    # tipoPresenza = PresenceType(name="provapresenza",percentageIncrease= 20,hourlyPay=10)
    # logging.info(PresenceTypeDao.createPresenceType(tipoPresenza))
    # tipoPresenzaDaAggiornare = PresenceType(id_tipoPresenza=5, nomeTipoPresenza="provapresenza",percentageIncrease= 40,hourlyPay=10)
    # logging.info(PresenceTypeDao.updatePresenceType(tipoPresenzaDaAggiornare))
    # logging.info(PresenceTypeDao.deletePresenceType(5))

if __name__ == "__main__":
   test.main()