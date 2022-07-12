import sys,os
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api/Dao")
sys.path.append(os.getcwd()+"/CLOUDMARK/back-end/api")
from TipoPresenzaDao import TipoPresenzaDao
class TestTipoPresenza:
  def main():
      print(TipoPresenzaDao.getAllTipoPresenza())
    # print(TipoPresenzaDao.getTipoPresenzabyNomeTipoPresenza("festivo"))
    # tipoPresenza = TipoPresenza(nomeTipoPresenza="prova", percentualeMaggiorazione= 30, pagaOraria= 10)
    # TipoPresenzaDao.insertTipoPresenza(tipoPresenza)
    # TipoPresenzaDao.updateTipoAccount(tipoPresenza)
    # TipoPresenzaDao.deleteTipoPresenza("prova")
   
if __name__ == "__main__":
   TestTipoPresenza.main()