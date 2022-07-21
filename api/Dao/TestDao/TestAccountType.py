import logging

from AccountTypeDao import AccountTypeDao
from Model.AccountType import AccountType


class test_account_type_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        ####### TEST BusinessDao ######
        # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
        total = 0
        counter = 0
        
        # try:
        #     total += 1
        #     logging.info(AccountTypeDao.getAllAccountsType())
        #     counter += 1
        # except(RuntimeError, TypeError, NameError)  as e:
        #     logging.error("TypeAccountDao getAllAccountsType not passed")
        #     logging.exception(e)
        
        accountTypeCreate = AccountType(id_account_type=3, accountTypeName='prova', function='prrr')
        
        try:
            total += 1
            logging.info(AccountTypeDao.createAccountType(accountTypeCreate))
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeAccountDao createAccountType not passed")
            logging.exception(e)

        # try:
        #     total += 1
        #     logging.info(AccountTypeDao.getAccountTypeById(accountTypeCreate.id_account_type))
        #     counter += 1
        # except(RuntimeError, TypeError, NameError)  as e:
        #     logging.error("TypeAccountDao getAccountTypeById not passed")
        #     logging.exception(e)
        
        # try:
        #     total += 1
        #     accountTypeToUpdate = AccountType(id_account_type=accountTypeCreate.id_account_type, accountTypeName='notProva', function='notPrr')
        #     AccountTypeDao.updateAccountType(accountTypeToUpdate)
        #     counter += 1
        # except(RuntimeError, TypeError, NameError)  as e:
        #     logging.error("TypeAccountDao updateAccountType not passed")
        #     logging.exception(e)
        
        # try:
        #     total += 1
        #     AccountTypeDao.deleteAccountType(accountTypeCreate.id_account_type)
        #     counter += 1
        # except(RuntimeError, TypeError, NameError)  as e:
        #     logging.error("TypeAccountDao deleteAccountType not passed")
        #     logging.exception(e)

        logging.warning("Test TypeAccountDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)       
