import logging
from unicodedata import name
from ContractTypeDAO import ContractTypeDAO
from Model.ContractType import ContractType

class test_contract_dao:
    def main(*args):
        logging.getLogger().setLevel(args[0])
        ####### TEST BusinessDao ######
        # in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
        total = 0
        counter = 0

        try:
            total += 1
            logging.info(ContractTypeDAO.getAllContractsType())
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getAllBusiness not passed")
            logging.exception(e)
            
        contractTypeCreate = ContractType(id_contractType=4,name="chiamata",info="aaa")
        
        try:
            total += 1
            ContractTypeDAO.createContractType(contractTypeCreate)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("TypeContractDao createContract not passed")
            logging.exception(e)
            
            
        try:
            total += 1
            ContractTypeDAO.getContractTypeByID(contractTypeCreate.id_contractType)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getContractTypeByID not passed")
            logging.exception(e)
            
        try:
            total += 1
            contractToUpdate = ContractType(id_contractType= contractTypeCreate.id_contractType,name="JOBS ACT",info = "CDM") 
            ContractTypeDAO.updateContractTypeById(contractToUpdate)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getContractTypeByID not passed")
            logging.exception(e)
       
        try:
            total += 1 
            ContractTypeDAO.deleteContractTypeById(contractToUpdate.id_contractType)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getContractTypeByID not passed")
            logging.exception(e)    
            
            
            
        logging.warning("Test TypeContractDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)


if __name__ == "__main__":
   test_contract_dao.main() 