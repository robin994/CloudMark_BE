import logging

from Model.PresenceModel import NewPresenceModel, PresenceModel
from PresenceDao import PresenceDao


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
            
        createPresence = NewPresenceModel(id_employee="12555467-e85b-1fd3-a456-333322233412",date_presence="2022-06-05",id_tipoPresenza =2, id_order="124e4567-e44f-1fd3-a456-330002223341",hours=5)
        
        try:
            total += 1
            uuidPresence = PresenceDao.createPresence(createPresence)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("PresenceDao createPresence not passed")
            logging.exception(e)
            
            
        try:
            total += 1
            PresenceDao.getPresenceByPrimaryKey(str(uuidPresence),createPresence.id_employee)
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
            PresenceDao.deletePresenceByPK(str(uuidPresence),str(createPresence.id_employee))
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceDao deletePresence not passed")
            logging.exception(e)    
            
            
            
        logging.warning("Test PresenceDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)


if __name__ == "__main__":
   test_presence_dao.main() 
