import logging
from unicodedata import name
from uuid import uuid4
from api.Dao.TestDao.TestAD import test_account_dao
from api.Dao.TestDao.TestBD import test_business_dao
from api.Dao.TestDao.TestOD import test_order_dao
from api.Dao.TestDao.TestCONTRACT import test_contract_dao



class test:
  def main():
    
    logging_level = logging.WARNING
    test_account_dao.main(logging_level)
    test_business_dao.main(logging_level)
    test_order_dao.main(logging_level)
    test_contract_dao.main(logging_level)

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