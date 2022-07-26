import logging
from Model.ContractType import ContractTypeModel
from ContractTypeDAO import ContractTypeDAO
from Model.ContractType import NewContractTypeModel


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
            
        contractTypeCreate = NewContractTypeModel(name="chiamata",info="aaa")
        
        try:
            total += 1
            CType = ContractTypeDAO.createContractType(contractTypeCreate)
            counter += 1
        except(RuntimeError, TypeError, NameError) as e:
            logging.error("TypeContractDao createContract not passed")
            logging.exception(e)
            
            
        try:
            total += 1
            uuid = str(CType["response"])
            ContractTypeDAO.getContractTypeByID(uuid)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getContractTypeByID not passed")
            logging.exception(e)
            
        try:
            total += 1
            contractToUpdate = ContractTypeModel(id_contract_type=uuid,name="JOBS ACT",info = "CDM") 
            ContractTypeDAO.updateContractTypeById(contractToUpdate)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getContractTypeByID not passed")
            logging.exception(e)
       
        try:
            total += 1 
            ContractTypeDAO.deleteContractTypeById(uuid)
            counter += 1
        except(RuntimeError, TypeError, NameError)  as e:
            logging.error("TypeContractDao getContractTypeByID not passed")
            logging.exception(e)    
            
            
            
        logging.warning("Test TypeContractDao, completati con successo %d / %d", counter, total)
        return dict(totals = total, counters = counter)


if __name__ == "__main__":
   test_contract_dao.main() 
