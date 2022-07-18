from fastapi.middleware.cors import CORSMiddleware
# from Dao.TipoPresenzaDao import TipoPresenzaDao
from Dao.TipoAccountDao import TipoAccountDao
# from Dao.PresenceDao import PresenceDao
from Dao.BusinessDao import BusinessDao
from Dao.EmployeeDAO import EmployeeDAO
from Dao.AccountDao import AccountDao
from Dao.CommessaDAO import CommessaDAO
from fastapi import FastAPI
from Dao.CustomerDao import CustomerDao
from api.Model.CustomerModel import CustomerModel
from api.Model.BusinessModel import BusinessModel
from api.Model.AccountModel import AccountModel, NewAccountModel
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

#Endpoint - Account
@app.get("/account", tags=["account"])
async def get_all_accounts():
    return AccountDao.getAllAccounts()

@app.get("/account/{uuid}", tags=["account"])
async def get_accounts_by_uuid(uuid):
    return AccountDao.getAccountByID(uuid)

@app.post("/account/signin", tags=["account"])
async def create_account(account : NewAccountModel):
    return AccountDao.createAccount(account)

@app.patch("/account/update", tags=["account"])
async def update_account(account : AccountModel, session: str):
    return AccountDao.updateAccount(account, session)

@app.post("/account/login", tags=["account"])
async def get_session(user : UserModel):
    return AccountDao.getSession(user)

@app.post("/account/delete", tags=["account"])
async def delete_account(id_account):
    return AccountDao.deleteAccountByID(id_account)

@app.post("/account/verify_account", tags=["account"])
async def jwt_verify(token: str):
    return AccountDao.jwt_verify(token)

# Endpoint - Business

@app.get("/business", tags=["business"])
async def get_all_business():
    return BusinessDao.getAllBusiness()

@app.post("/business/", tags=["business"])
async def filter_by_business(business : BusinessModel):
    return BusinessDao.filterByBusiness(business)

@app.post("/business/create", tags=["business"])
async def create_business(business : BusinessModel):
    return BusinessDao.createBusiness(business)  

# @app.post("/business/update", tags=["business"])
# async def update_business(business : BusinessModel):
#     return BusinessDao.updateBusinessById(business)      

@app.post("/business/delete", tags=["business"])
async def delete_business(id_business):
    return BusinessDao.deleteBusinessById(id_business)

#Endpoint - Commessa

@app.get("/orders", tags=["orders"])
async def get_all_orders():
    return CommessaDAO.getAllOrders()
    
# @app.get("/presence")
# async def getAllPresence():
#     return PresenceDao.getAllPresence()

# Endpoint - Customer

@app.get("/customer", tags=["customer"])
async def get_all_customer():
    return CustomerDao.getAllCustomers()

# @app.get("/customer/byBusinessId", tags=["customer"])
# async def get_all_customer_by_business_id():
#     return CustomerDao.getCustomerByBusinessID()    

@app.post("/customer/create", tags=["customer"])
async def create_customer(customer : CustomerModel):
    return CustomerDao.createCustomer(customer)

@app.post("/customer/delete", tags=["customer"])
async def delete_customer(id_customer):
    return CustomerDao.deleteCustomerByID(id_customer)

# Endpoint - Employee

@app.get("/employee", tags=["employee"])
async def get_all_employees():
    return EmployeeDAO.getAllEmployees()

@app.post('/employee/', tags=["employee"] )
async def filter_by_employee(Employee : EmployeeModel, idAzienda: int):
    return EmployeeDAO.filterByEmployee(Employee, idAzienda)

@app.get("/employee/lastwork", tags=["employee"])
async def get_employees_by_last_work():
    return EmployeeDAO.getEmployeesByLastWork()

# Endpoint - TipoAccount

@app.get("/type/account", tags=["Type"])
async def get_all_tipo_account():
    return TipoAccountDao.getAllTipoAccount()

@app.post("/type/account/{id_account}", tags=["Type"])
async def get_tipo_account_by_id(id_account):
    return TipoAccountDao.getTipoAccountByIdTipoAccount(id_account)