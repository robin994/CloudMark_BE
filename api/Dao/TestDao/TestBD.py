import logging

from BusinessDao import BusinessDao
from Model.BusinessModel import BusinessModel, NewBusinessModel


class test_business_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        ####### TEST BusinessDao ######
        # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
        total = 0
        counter = 0

        try:
            total += 1
            BusinessDao.getAllBusiness()
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("BusinessDao getAllBusiness not passed")
            logging.exception(e)
            
        businessCreate = NewBusinessModel(name='TechHub', p_iva='498484894', address='via Salimberi 1', cap='00321', iban="846541515121",phone="065454554" ,email="techub@mail.it", pec="techub@pec.it", fax="0645454545")
        
        try:
            total += 1
            uuidBusiness = BusinessDao.createBusiness(businessCreate)
            logging.debug("BusinessDao createBusiness:" + str(uuidBusiness))
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("BusinessDao createBusiness not passed")
            logging.exception(e)

        
        try:
            total += 1
            BusinessDao.getBusinessByID(str(uuidBusiness))
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("BusinessDao getBusinessByID not passed")
            logging.exception(e)

        try:
            total += 1
            businessUpdate = BusinessModel(id_business=str(uuidBusiness), name='PeppeHub', p_iva='498484894', address='via Salimberi 1', cap='00321', iban="846541515121",phone="065454554" ,email="techub@mail.it", pec="techub@pec.it", fax="0645454545")
            BusinessDao.updateBusinessById(businessUpdate)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("BusinessDao updateBusinessByID not passed")
            logging.exception(e)

        try:
            total += 1
            toSearch : BusinessModel = BusinessModel(name= "m",p_iva= "",address="",cap= "",iban= "",phone= "",email= "",pec= "",fax= "",id_business= "")
            logging.info(BusinessDao.filterByBusiness(toSearch))
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("BusinessDao filterByBusiness not passed")
            logging.exception(e)
        
        try:
            total += 1
            BusinessDao.deleteBusinessById(uuidBusiness)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("BusinessDao deleteBusinessByID not passed")
            logging.exception(e)
        
        logging.warning("Test BusinessDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)

if __name__ == "__main__":
   test_business_dao.main() 
