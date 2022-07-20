import logging
from unicodedata import name
from PresenceDao import PresenceDao
from Model.PresenceModel import PresenceModel

class test_presence_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        ####### TEST BusinessDao ######
        # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
        total = 0
        counter = 0

        try:
            total += 1
            logging.info(PresenceDao.getAllPresence())
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceDao getAllBPresences not passed")
            logging.exception(e)
            
        createPresence = PresenceModel(id_employee="12555467-e85b-1fd3-a456-333322233412",date_presence="2022-05-05",id_tipoPresenza =2, id_order="124e4567-e44f-1fd3-a456-330002223341",hours=5)
        
        try:
            total += 1
            PresenceDao.createPresence(createPresence)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("PresenceDao createPresence not passed")
            logging.exception(e)
            
            
        try:
            total += 1
            PresenceDao.getPresenceByPrimaryKey(createPresence.id_employee,createPresence.date_presence,createPresence.id_tipoPresenza)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceDao getPresenceByPK not passed")
            logging.exception(e)
            
        try:
            total += 1
            presenceUpdate = PresenceModel(id_employee=createPresence.id_employee,date_presence=createPresence.date_presence,id_tipoPresenza=createPresence.id_tipoPresenza,id_order=createPresence.id_order,hours=500) 
            PresenceDao.updatePresenceByIDEmployeeAndDate(presenceUpdate)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceDao updatePresence not passed")
            logging.exception(e)
       
        try:
            total += 1 
            PresenceDao.deletePresenceByPK(id_employee=createPresence.id_employee,datePresence=createPresence.date_presence,id_typePresence=createPresence.id_tipoPresenza)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceDao deletePresence not passed")
            logging.exception(e)    
            
            
            
        logging.warning("Test PresenceDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)


if __name__ == "__main__":
   test_presence_dao.main() 