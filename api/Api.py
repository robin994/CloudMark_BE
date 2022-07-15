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
from api.Model.UserModel import UserModel

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

@app.get('/employee/{firstname}/{lastname}')
async def get_employee_by_name_surname(firstname, lastname):
    return EmployeeDAO.getEmployeeByNameSurname(firstname, lastname)

@app.get('/employee/{lastname}')
async def get_employee_by_surname(lastname):
    return EmployeeDAO.getEmployeeBySurname(lastname)

@app.get('/codicefiscale/{cf}')
async def get_employee_by_cf(cf):
    return EmployeeDAO.getEmployeeByCF(cf)

@app.get('/matricola/{matricola}')
async def get_employee_by_employee(matricola:str):
    return EmployeeDAO.getEmployeeByMatricola(matricola)
@app.get("/fine/rapporto")
async def get_employees_by_last_work():
    return EmployeeDAO.getEmployeesByLastWork()






@app.get("/customer")
async def getAllCustomer():
    return CustomerDao.getAllCustomers()

@app.get("/business")
async def getAllBusiness():
    return BusinessDao.getAllBusiness()

@app.get("/business")
async def getAllBusiness():
    return BusinessDao.getAllBusiness()

@app.post("/account/")
async def getSession(user : UserModel):
    return AccountDao.getSession(user)

@app.get("/commessa")
async def getAllOrders():
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