import logging
from CustomerDao import CustomerDao
from Model.CustomerModel import CustomerModel, NewCustomerModel

class test_customer_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        ##### TEST AccountDAO ######
        #in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
        total = 0
        counter = 0

        try:
            total += 1
            CustomerDao.getAllCustomers()
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("CustomerDao getAllCustomer not passed")
            logging.exception(e)

        customerCreate = NewCustomerModel(name='Gino', p_iva='498458741', address='via Bindiri 7', cap='00874', iban="12345568975",phone="062131214" ,email="newgino@mail.it", pec="newgino@pec.it", fax="062131521")   

        try:
            total += 1
            uuidCustomer = CustomerDao.createCustomer(customerCreate)
            logging.debug("CustomerDao createCustomer:" + str(uuidCustomer))
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("CustomerDao createCustomer not passed")
            logging.exception(e) 

        try:
            total += 1
            CustomerDao.getCustomerByID(str(uuidCustomer))
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("CustomerDao getCustomerByID not passed")
            logging.exception(e)

        try:
            total += 1
            CustomerDao.getCustomerByBusinessID(str(uuidCustomer))
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("CustomerDao getCustomerByBusinessID not passed")
            logging.exception(e)

        try:
            total += 1
            customerUpdate = CustomerModel(id_customer=str(uuidCustomer), name='NewGino', p_iva='498458741', address='via Bindiri 7', cap='00874', iban="12345568975",phone="062131214" ,email="newgino@mail.it", pec="newgino@pec.it", fax="062131521")
            CustomerDao.updateCustomerByID(customerUpdate)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("CustomerDao updateCustomerByID not passed")
            logging.exception(e)

        try:
            total += 1
            CustomerDao.deleteCustomerByID(str(uuidCustomer))
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("CustomerDao deleteCustomerByID not passed")
            logging.exception(e)
        
        logging.warning("Test CustomerDao, completati con successo %d / %d", counter, total)            

if __name__ == "__main__":
   test_customer_dao.main()         