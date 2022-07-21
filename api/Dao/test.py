import logging

from api.Dao.TestDao.TestAccountType import test_account_type_dao
from api.Dao.TestDao.TestAD import test_account_dao
from api.Dao.TestDao.TestBD import test_business_dao
from api.Dao.TestDao.TestCONTRACT import test_contract_dao
from api.Dao.TestDao.TestCustomer import test_customer_dao
from api.Dao.TestDao.TestED import test_employee_dao
from api.Dao.TestDao.TestOD import test_order_dao
from api.Dao.TestDao.TestPRESENCE import test_presence_dao
from api.Dao.TestDao.TestPresenceType import test_presence_type_dao


class test:
  def main():
    results =dict(total = 0 , counter = 0)
    logging_level = logging.WARNING
    test.addResults(test_presence_dao.main(logging_level), results)
    test.addResults(test_account_dao.main(logging_level), results)
    test.addResults(test_business_dao.main(logging_level), results)
    test.addResults(test_order_dao.main(logging_level), results)
    test.addResults(test_contract_dao.main(logging_level), results)
    test.addResults(test_customer_dao.main(logging_level), results)
    test.addResults(test_presence_type_dao.main(logging_level), results)
    # test.addResults(test_employee_dao.main(logging_level), results)
    test.addResults(test_account_type_dao.main(logging_level), results) 

    if results["counter"] == results["total"]:
      logging.warning("Congratulazioni test completati con successo")
    else:
      logging.warning("test incompleti")
      logging.warning("test fatti: %s", results["total"])
      logging.warning("test completati con successo: %s", results["counter"])

  @staticmethod
  def addResults(test: dict, resutls:dict):
    resutls["counter"] += test["counters"]
    resutls["total"] += test["totals"]
    return resutls
      
   
   

if __name__ == "__main__":
   test.main()
