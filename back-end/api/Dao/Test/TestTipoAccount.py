import sys,os
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api/Dao")
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api")
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api/Model")
from TipoAccountDao import TipoAccountDao
from Model.TipoAccount import TipoAccount
class TestTipoAccount:
   def main():
    print(TipoAccountDao.getAllTipoAccount())
    # print(TipoAccountDao.getTipoAccountByNomeTipoAccount("administrator"))
    # ta = TipoAccount(nomeTipoAccount = "prova", funzioneProfilo = "scaccomatto")
    # TipoAccountDao.insertTipoAccount(ta)
    # TipoAccountDao.updateTipoAccount(ta)
    # TipoAccountDao.deleteTipoAccount("prova")
    
    print
if __name__ == "__main__":
    TestTipoAccount.main()
    
   