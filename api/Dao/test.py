from EmployeeDAO import EmployeeDAO
from AccountDao import AccountDao
from Model.AccountModel import AccountModel
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
    logging.warning(EmployeeDAO.getAllEmployees())
    # logging.warning(EmployeeDAO.getEmployeeByID(1))
    # logging.warning(EmployeeDAO.getEmployeeByNameSurname('Bruno', 'Rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByCF('123'))
    # logging.warning(EmployeeDAO.getEmployeeBySurname('Rossi'))
    # logging.warning(EmployeeDAO.getEmployeeByMatricola('0000'))

if __name__ == "__main__":
   test.main()