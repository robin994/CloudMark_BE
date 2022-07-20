import logging
from PresenceTypeDao import PresenceTypeDao
from Model.PresenceType import PresenceType

class test_presence_type_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        ####### TEST PresenceTypeDao ######
        # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
        total = 0
        counter = 0

        try:
            total += 1
            logging.info(PresenceTypeDao.getAllPresenceType())
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceTypeDao getAllPresenceType not passed")
            logging.exception(e)

        createPresenceType = PresenceType(name="permesso",percentageIncrease=0,hourlyPay=8)

        try:
            total += 1
            PresenceTypeDao.createPresenceType(createPresenceType)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("PresenceTypeDao createPresenceType not passed")
            logging.exception(e)    

        try:
            total += 1
            PresenceTypeDao.getPresenceTypebyId(1)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceTypeDao getPresenceTypeByID not passed")
            logging.exception(e)

        try:
            total += 1
            presenceTypeUpdate = PresenceType(id_presenceType=1, name='orario standard', percentageIncrease=0, hourlyPay=8)
            PresenceTypeDao.updatePresenceType(presenceTypeUpdate)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceTypeDao updatePresenceTypeByID not passed")
            logging.exception(e)

        try:
            total += 1
            PresenceTypeDao.deletePresenceType(5)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("PresenceTypeDao deletePresenceTypeByID not passed")
            logging.exception(e)

        logging.warning("Test PresenceTypeDao, completati con successo %d / %d", counter, total)


if __name__ == "__main__":
   test_presence_type_dao.main()                 