import sys,os
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api/Dao")
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api")
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api/Model")
from TipoPresenzaDao import TipoPresenzaDao
from Model.TipoPresenza import TipoPresenza
class TestTipoPresenza:
  def main():
    print(TipoPresenzaDao.getAllTipoPresenza())
    print(TipoPresenzaDao.getTipoPresenzabyNomeTipoPresenza("festivo"))
    # tipoPresenza = TipoPresenza(nomeTipoPresenza="aa", percentualeMaggiorazione= 30, pagaOraria= 10)
    # TipoPresenzaDao.insertTipoPresenza(tipoPresenza)
    # TipoPresenzaDao.updateTipoAccount(tipoPresenza)
    # TipoPresenzaDao.deleteTipoPresenza("prova")
   
if __name__ == "__main__":
   TestTipoPresenza.main()