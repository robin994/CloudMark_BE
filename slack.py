from fastapi import FastAPI
from Model.ContractType import NewContractTypeModel, ContractTypeModel
from Dao.AccountTypeDao import AccountTypeDao
from Dao.ContractTypeDAO import ContractTypeDAO
from Dao.CustomerDao import CustomerDao
from Dao.PresenceDao import PresenceDao
from Dao.PresenceTypeDao import PresenceTypeDao
from Model.PresenceModel import LoadPresenceModel, NewPresencesModel, PresenceModel
from Model.AccountType import AccountType, NewAccountType
from Dao.AccountTypeDao import AccountTypeDao
from Model.AccountModel import AccountModel, NewAccountModel
from Model.BusinessModel import BusinessModel, NewBusinessModel
from Model.CustomerModel import CustomerModel, NewCustomerModel
from Model.EmployeeModel import EmployeeModel, NewAccountEmployeeModel, NewEmployeeModel
from Model.OrderModel import NewOrderModel, OrderModel
from Model.PresenceModel import NewPresenceModel
from Model.UserModel import ResetPasswordModel, UserModel
from Model.PresenceTypeModel import NewPresenceTypeModel, PresenceTypeModel
from Model.UserModel import UserModel
from Dao.AccountDao import AccountDao
from Dao.AccountTypeDao import AccountTypeDao
from Dao.BusinessDao import BusinessDao
from Dao.ContractTypeDAO import ContractTypeDAO
from Dao.CustomerDao import CustomerDao
from Dao.EmployeeDAO import EmployeeDAO
from Dao.OrderDao import OrderDao
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# #Per risolvere il problema del cors policy indico su quale path si trova il FE (Modificare la porta in base alle impostazioni locali)
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

@app.post("/account/signin/", tags=["account"])
async def create_account(account : NewAccountModel):
    return AccountDao.createAccount(account)

@app.patch("/account/update/", tags=["account"])
async def update_account(account : AccountModel, session: str):
    return AccountDao.updateAccount(account, session)

@app.patch("/account/reset_passowrd", tags=["account"])
async def reset_password(password : ResetPasswordModel):
    return AccountDao.resetPassword(password)

@app.post("/account/login", tags=["account"])
async def get_session(user : UserModel):
    return AccountDao.getSession(user)

@app.post("/account/delete/", tags=["account"])
async def delete_account(id_account):
    return AccountDao.deleteAccountByID(id_account)

@app.post("/account/verify_account", tags=["account"])
async def jwt_verify(token: str):
    return AccountDao.jwt_verify(token)

# Endpoint - Business

@app.get("/business", tags=["business"])
async def get_all_business():
    return BusinessDao.getAllBusiness()

@app.get("/business/{uuid}", tags=["business"])
async def get_business_by_id(uuid):
    return BusinessDao.getBusinessByID(uuid)

@app.post("/business/", tags=["business"])
async def filter_by_business(business : BusinessModel):
    return BusinessDao.filterByBusiness(business)

@app.post("/business/create/", tags=["business"])
async def create_business(business : NewBusinessModel):
    return BusinessDao.createBusiness(business)  

@app.post("/business/update/", tags=["business"])
async def update_business(business : BusinessModel):
    return BusinessDao.updateBusinessById(business)      

@app.post("/business/delete/", tags=["business"])
async def delete_business(id_business:str):
    return BusinessDao.deleteBusinessById(id_business)

@app.post("/business/customer/", tags=["business"])
async def get_all_business_by_customer_id(customer_uuid):
    return BusinessDao.getBusinessByCustomerID(customer_uuid)    

#Endpoint - Commessa

@app.get("/orders", tags=["orders"])
async def get_all_orders():
    return OrderDao.getAllOrders()

@app.get("/orders/{uuid}", tags=["orders"])
async def get_order_by_id(uuid):
    return OrderDao.getOrderByID(uuid)

@app.post("/orders/create/", tags=["orders"])
async def create_order(order : NewOrderModel):
    return OrderDao.createOrder(order)  

@app.post("/orders/update/", tags=["orders"])
async def update_order(order : OrderModel):
    return OrderDao.updateOrderById(order)      

@app.post("/orders/delete/", tags=["orders"])
async def delete_order(id_order:str):
    return OrderDao.deleteOrderByID(id_order)

@app.get("/orders/employee/{id_employee}", tags=["orders"])
async def get_order_by_employee(id_employee):
    return OrderDao.getOrderByEmplyee(id_employee)

# Endpoint - Customer

@app.get("/customer", tags=["customer"])
async def get_all_customer():
    return CustomerDao.getAllCustomers()

@app.post("/customer/business/{business_uuid}", tags=["customer"])
async def get_all_customer_by_business_id(business_uuid):
    return CustomerDao.getCustomerByBusinessID(business_uuid)    

@app.post("/customer/{uuid}", tags=["customer"])
async def get_by_id(uuid):
    return CustomerDao.getCustomerByID(uuid)  

@app.post("/customer/create/", tags=["customer"])
async def create_customer(customer : NewCustomerModel):
    return CustomerDao.createCustomer(customer)

@app.post("/customer/delete/", tags=["customer"])
async def delete_customer(id_customer: str):
    return CustomerDao.deleteCustomerByID(id_customer)

@app.post("/customer/update/", tags=["customer"])
async def update_customer_by_id(customer: CustomerModel):
    return CustomerDao.updateCustomerByID(customer)

# Endpoint - Employee

@app.get("/employee", tags=["employee"])
async def get_all_employees():
    return EmployeeDAO.getAllEmployees()

@app.get("/employee/all", tags=["employee"])
async def get_all_employees_by_empty_key():
    return EmployeeDAO.getAllEmployeesByEmptyKey()

@app.post('/employee/', tags=["employee"])
async def filter_by_employee(employee : NewEmployeeModel, idAzienda: str):
    return EmployeeDAO.filterByEmployee(employee, idAzienda)

@app.get("/employee/lastwork", tags=["employee"])
async def get_employees_by_last_work():
    return EmployeeDAO.getEmployeesByLastWork()

@app.get("/employee/business/{id_business}", tags=["employee"])
async def get_employees_by_business(id_business):
    return EmployeeDAO.getEmployeesByBusiness(id_business)

@app.get("/employee/account/{id_account}", tags=["employee"])
async def get_employees_by_account(id_account):
    return EmployeeDAO.getEmployeesByAccount(id_account)

@app.get("/employee/{id_business}", tags=["employee"])
async def get_employees_by_id(id_business):
    return EmployeeDAO.getEmployeesByID(id_business)

@app.post('/employee/create/', tags=["employee"])
async def create_employee(employee : NewEmployeeModel):
    return EmployeeDAO.createEmployee(employee)

@app.post('/employee/update/', tags=["employee"])
async def update_employee_by_id(employee : EmployeeModel):
    return EmployeeDAO.updateEmployeeByID(employee)

@app.post('/employee/delete/', tags=["employee"])
async def delete_employee_by_id(id_employee: str):
    return EmployeeDAO.deleteEmployeeByID(id_employee)

@app.post('/employee/create/account', tags=["employee"])
async def create_new_account_employee(payload : NewAccountEmployeeModel):
    return EmployeeDAO.createNewAccountEmployee(payload)

# Endpoint - AccountType

@app.get("/type/account", tags=["Type Account"])
async def get_all_tipo_account():
    return AccountTypeDao.getAllAccountsType()

@app.post("/type/account/{id_account_type}", tags=["Type Account"])
async def get_tipo_account_by_id(id_account_type):
    return AccountTypeDao.getAccountTypeById(id_account_type)

@app.post("/type/account/create/", tags=["Type Account"])
async def create_account_type(accountType: NewAccountType):
    return AccountTypeDao.createAccountType(accountType)

@app.post("/type/account/update/", tags=["Type Account"])
async def update_account_type(accountType: AccountType):
    return AccountTypeDao.updateAccountType(accountType)

@app.post("/type/account/delete/", tags=["Type Account"])
async def delete_account_type(id_type_account):
    return AccountTypeDao.deleteAccountType(id_type_account)

# Endpoint - ContractType

@app.get("/type/contract", tags=["Type Contract"])
async def get_all_contract_type():
    return ContractTypeDAO.getAllContractsType()

@app.post("/type/contract/{id_contract}", tags=["Type Contract"])
async def get_contract_type_by_id(id_contract):
    return ContractTypeDAO.getContractTypeByID(id_contract)

@app.post("/type/contract/create/", tags=["Type Contract"])
async def create_contract_type(contractType: NewContractTypeModel):
    return ContractTypeDAO.createContractType(contractType)

@app.post("/type/contract/update/", tags=["Type Contract"])
async def update_contract_type_by_ID(contractType: ContractTypeModel):
    return ContractTypeDAO.updateContractTypeById(contractType)

@app.post("/type/contract/delete/", tags=["Type Contract"])
async def delete_contract_type_by_ID(id_contract):
    return ContractTypeDAO.deleteContractTypeById(id_contract)

# Endpoint - Presence

@app.get("/presence/{id_presence}/{id_employee}", tags=["Presence"])
async def get_presence_by_primary_key(id_presence, id_employee):
    return PresenceDao.getPresenceByPrimaryKey(id_presence, id_employee)

@app.get("/presence/all", tags=["Presence"])
async def get_all_presence():
    return PresenceDao.getAllPresence()

@app.get("/presence/load_employee={id_employee}", tags=["Presence"])
async def get_presences_by_employee(id_employee:str):
    return PresenceDao.getPresencesByEmployee(id_employee)

@app.post("/presence/load", tags=["Presence"])
async def get_month_year_presences(load_presence_model: LoadPresenceModel):
    return PresenceDao.getMonthYearPresences(load_presence_model)

@app.post("/presence/create", tags=["Presence"])
async def create_presence(presence: NewPresenceModel):
    return PresenceDao.createPresence(presence)

@app.post("/presence/update/", tags=["Presence"])
async def update_presence(presence: PresenceModel):
    return PresenceDao.updatePresenceByIDEmployeeAndDate(presence)

@app.post("/presence/delete/", tags=["Presence"])
async def delete_presence(id_presence, id_employee):
    return PresenceDao.deletePresenceByPK(id_presence, id_employee)

@app.post("/prova", tags=["Presence"])
async def provino(payload: NewPresencesModel):
    return PresenceDao.insert_or_delete_presence(payload)

# Endpoint - PresenceType

@app.get("/type/presence", tags=["Type Presence"])
async def get_all_presence_type():
    return PresenceTypeDao.getAllPresenceType()

@app.get("/type/presence/id/{id_presence_type}", tags=["Type Presence"])
async def get_presence_type_by_id(id_presence_type):
    return PresenceTypeDao.getPresenceTypebyId(id_presence_type)

@app.post("/type/presence/create/", tags=["Type Presence"])
async def create_presence_type(typePresence: NewPresenceTypeModel):
    return PresenceTypeDao.createPresenceType(typePresence)

@app.patch("/type/presence/update/", tags=["Type Presence"])
async def update_presence_type(typePresence: PresenceTypeModel):
    return PresenceTypeDao.updatePresenceType(typePresence)

@app.post("/type/presence/delete/", tags=["Type Presence"])
async def delete_presence_type(id_presence_type):
    return PresenceTypeDao.deletePresenceType(id_presence_type)