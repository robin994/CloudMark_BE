import logging

from AccountDao import AccountDao
from Model.AccountModel import AccountModel, NewAccountModel
from Model.UserModel import UserModel


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
   except(RuntimeError, TypeError, NameError)  as e:
     logging.error("AccountDaio getAllAccounts not passed")
     logging.exception(e)
     
   accountCreate = NewAccountModel(user="Franco", password='aaaa', abilitato=1,id_tipo_account="7e554b54-08f4-11ed-861d-0242ac120002") 
       
   try:
     total += 1
     uuidAccount = AccountDao.createAccount(accountCreate)
     logging.debug("Acccount Create:" + str(uuidAccount))
     counter += 1
   except(RuntimeError, TypeError, NameError) as e:
     logging.error("AccountDaio createAccount not passed")
     logging.exception(e)
   
   try:
     total += 1
     uuid = str(uuidAccount["response"])
     logging.debug(uuid)
     AccountDao.getAccountByID(uuid)
     counter += 1
   except(RuntimeError, TypeError, NameError)  as e:
     logging.error("AccountDaio getAccountByID not passed")
     logging.exception(e)
     
   try:
     total += 1
     session = AccountDao.getSession(UserModel(user='Franco', password='aaaa') )
     logging.debug("sesssion: "+ str(session))
     counter += 1
   except(RuntimeError, TypeError, NameError)  as e:
     logging.error("AccountDaio getSession not passed")
     logging.exception(e)

   try:
     total += 1
     accountUpdate = AccountModel(id_account= uuid, user="Beppe", password='aaaa', abilitato=1,id_tipo_account=1)
     AccountDao.updateAccount(accountUpdate, session)
     counter += 1
   except(RuntimeError, TypeError, NameError)  as e:
     logging.error("AccountDaio updateAccountByID not passed")
     logging.exception(e)
   
   try:
     total += 1
     AccountDao.deleteAccountByID(uuid)
     counter += 1
   except(RuntimeError, TypeError, NameError)  as e:
     logging.error("AccountDaio deleteAccountByID not passed")
     logging.exception(e)
   logging.warning("Test AccountDao, completati con successo %d / %d", counter, total)
   return dict(totals = total, counters = counter)
 
 
 
if __name__ == "__main__":
   test_account_dao.main()
