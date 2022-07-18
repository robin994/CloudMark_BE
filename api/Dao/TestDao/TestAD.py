import logging
from AccountDao import AccountDao
from Model.UserModel import UserModel
from Model.AccountModel import AccountModel, NewAccountModel

class test_account_dao:
  def main(*args):
   logging.getLogger().setLevel(args[0])
   ##### TEST AccountDAO ######
   #in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
   total = 0
   counter = 0

   try:
     total += 1
     AccountDao.getAllAccounts()
     counter += 1
   except(RuntimeError, TypeError, NameError):
     logging.error("AccountDaio getAllAccounts not passed")
     
   accountCreate = NewAccountModel(user="Franco", password='aaaa', abilitato=1, id_tipoAccount=1)
       
   try:
     total += 1
     uuidAccount = AccountDao.createAccount(accountCreate)
     print(uuidAccount)
     counter += 1
   except(RuntimeError, TypeError, NameError):
     logging.error("AccountDaio createAccount not passed")
   
   try:
     total += 1
     AccountDao.getAccountByID('e55917e1-0e9f-40b2-92ae-c880328aa110')
     counter += 1
   except(RuntimeError, TypeError, NameError):
     logging.error("AccountDaio getAccountByID not passed")
     
   try:
     total += 1
     session = AccountDao.getSession(UserModel(user='Franco', password='aaaa') )
     counter += 1
   except(RuntimeError, TypeError, NameError):
     logging.error("AccountDaio getSession not passed")

   try:
     total += 1
     accountUpdate = AccountModel(id_account=str(uuidAccount), user="Beppe", password='aaaa', abilitato=1, id_tipoAccount=1)
     AccountDao.updateAccount(accountUpdate, session)
     counter += 1
   except(RuntimeError, TypeError, NameError):
     logging.error("AccountDaio updateAccountByID not passed")
   
   try:
     total += 1
     AccountDao.deleteAccountByID(uuidAccount)
     counter += 1
   except(RuntimeError, TypeError, NameError):
     logging.error("AccountDaio deleteAccountByID not passed")
   logging.warning("Test AccountDao, completati con successo %d / %d", counter, total)
 
 
 
if __name__ == "__main__":
   test_account_dao.main()