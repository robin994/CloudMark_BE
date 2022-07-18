from fastapi.middleware.cors import CORSMiddleware
# from Dao.TipoPresenzaDao import TipoPresenzaDao
from Dao.TipoAccountDao import TipoAccountDao
# from Dao.BusinessDao import BusinessDao
# from Dao.AccountDao import AccountDao
# from Dao.PresenceDao import PresenceDao
from Dao.BusinessDao import BusinessDao
# from Dao.CustomerDao import CustomerDao
from Dao.EmployeeDAO import EmployeeDAO
from Dao.AccountDao import AccountDao
from Dao.CommessaDAO import CommessaDAO
from fastapi import FastAPI
from Dao.CustomerDao import CustomerDao
from api.Model.AccountModel import AccountModel
from api.Model.UserModel import UserModel
from api.Model.EmployeeModel import EmployeeModel

app = FastAPI()

#Per risolvere il problema del cors policy indico su quale path si trova il FE (Modificare la porta in base alle impostazioni locali)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    
    #lista di origins a cui è permesso fare richieste cross-origin
    allow_origins=origins,
    allow_credentials=True,
    
    #Lista di tutti i tipi di chiamate che il FE può effettuare (POST, GET, PUT, PATCH), * indica tutte.
    allow_methods=["*"],
    
    #Lista di Headers accettati (Accept, Accept-Language, Content-Language ...)
    allow_headers=["*"],
)

# Endpoint - Employee
@app.get("/employee")
async def get_all_employees():
    return EmployeeDAO.getAllEmployees()

@app.post('/employee/')
async def filter_by_employee(Employee : EmployeeModel, idAzienda: int):
    return EmployeeDAO.filterByEmployee(Employee, idAzienda)

@app.get("/fine/rapporto")
async def get_employees_by_last_work():
    return EmployeeDAO.getEmployeesByLastWork()

@app.get("/customer")
async def get_all_customer():
    return CustomerDao.getAllCustomers()

@app.get("/business")
async def get_all_business():
    return BusinessDao.getAllBusiness()


@app.post("/account/signin")
async def create_account(account : AccountModel):
    return AccountDao.createAccount(account)

@app.post("/account/login")
async def get_session(user : UserModel):
    return AccountDao.getSession(user)

@app.get("/commessa")
async def get_all_orders():
    return CommessaDAO.getAllOrders()
    
# @app.get("/presence")
# async def getAllPresence():
#     return PresenceDao.getAllPresence()



# Endpoint - TipoAccount
@app.get("/tipo/account")
async def get_all_tipo_account():
    return TipoAccountDao.getAllTipoAccount()

@app.get("/tipo/account/{id_account}")
async def get_tipo_account_by_id(id_account):
    return TipoAccountDao.getTipoAccountByNomeTipoAccount(id_account)