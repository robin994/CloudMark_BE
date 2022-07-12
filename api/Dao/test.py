from AccountDao import AccountDao
import logging

class test:
  def main():
    logging.info("TEST ACCOUNT DAO")

    logging.warning(AccountDao.getAllAccounts())
   
if __name__ == "__main__":
   test.main()