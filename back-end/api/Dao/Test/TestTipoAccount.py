import imp
import logging
import importlib.util
import sys
sys.path.insert(0,'CloudMark/back-end/api/Dao')
from ...Dao.TipoAccountDao import TipoAccountDao

class ServiceAlex:
   def main():
    print(TipoAccountDao.getAllTipoAccount())
    # print(TipoAccountDao.getTipoAccountByNomeTipoAccount("administrator"))
    # ta = TipoAccount(nomeTipoAccount = "prova", funzioneProfilo = "scacco")
    # TipoAccountDao.insertTipoAccount(ta)
    # TipoAccountDao.deleteTipoAccount("prova")
    # print(TipoPresenzaDao.getTipoPresenzabyNomeTipoPresenza("festivo"))
    # tipoPresenza = TipoPresenza(nomeTipoPresenza="prova", percentualeMaggiorazione= 30, pagaOraria= 10)
    # TipoPresenzaDao.insertTipoPresenza(tipoPresenza)
    # TipoPresenzaDao.updateTipoAccount(tipoPresenza)
    # TipoPresenzaDao.deleteTipoPresenza("prova")
    
    print
if __name__ == "__main__":
    ServiceAlex.main()
    
   