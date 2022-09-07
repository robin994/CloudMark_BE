import json
from typing import List
from urllib import request
from fastapi import FastAPI,Query,Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Dao.AccountDao import AccountDao
from Dao.AccountTypeDao import AccountTypeDao
from Dao.BusinessDao import BusinessDao
from Dao.CallBackResponse import CallBackResponse
from Dao.ContractTypeDAO import ContractTypeDAO
from Dao.CustomerDao import CustomerDao
from Dao.EmployeeDAO import EmployeeDAO
from Dao.OrderDao import OrderDao
from Dao.PresenceDao import PresenceDao
from Dao.PresenceTypeDao import PresenceTypeDao
from Dao.OrderEmployee import OrderEmployee
from Model.AccountModel import AccountModel, NewAccountModel, OtherAccountModel
from Model.AccountType import AccountType, NewAccountType
from Model.BusinessModel import BusinessModel, NewBusinessModel
from Model.ContractType import ContractTypeModel, NewContractTypeModel
from Model.CustomerModel import CustomerModel, NewCustomerModel
from Model.EmployeeModel import (EmployeeModel, NewAccountEmployeeModel,
                                 NewEmployeeModel, EmployeeBusinessModel)
from Model.OrderEmployeeModel import NewOrderEmployee, OrderEmployeeModel as oem, UpdateOrderEmployeeModel, graphPayloadModel
from Model.OrderModel import NewOrderModel, OrderModel, CustomerIDBusinessIDModel, OrderEmployeeModel
from Model.PresenceModel import (LoadPresenceModel, NewPresenceModel,
                                 NewPresencesModel, PresenceModel)
from Model.PresenceTypeModel import NewPresenceTypeModel, PresenceTypeModel
from Model.UserModel import ResetPasswordModel, UserModel

app = FastAPI()

# #Per risolvere il problema del cors policy indico su quale path si trova il FE (Modificare la porta in base alle impostazioni locali)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,

    # lista di origins a cui è permesso fare richieste cross-origin
    allow_origins=origins,
    allow_credentials=True,

    # Lista di tutti i tipi di chiamate che il FE può effettuare (POST, GET, PUT, PATCH), * indica tutte.
    allow_methods=["*"],

    # Lista di Headers accettati (Accept, Accept-Language, Content-Language ...)
    allow_headers=["*"],
)


class dbcredentialModel(BaseModel):
    endpoint: str
    user: str
    password: str
    database: str


#Endpoint - Account
@app.get("/account", tags=["Account"])
async def get_all_accounts():
    return AccountDao.getAllAccounts()


@app.get("/account/{uuid}", tags=["Account"])
async def get_accounts_by_uuid(uuid):
    return AccountDao.getAccountByID(uuid)


@app.post("/account/signin/", tags=["Account"])
async def create_account(account: NewAccountModel, id_employee):
    return AccountDao.createAccount(account, id_employee)

@app.post("/account/update/", tags=["Account"])
async def update_account(account: OtherAccountModel, session: str):
    return AccountDao.updateAccount(account, session)


@app.patch("/account/reset_passowrd", tags=["Account"])
async def reset_password(password: ResetPasswordModel):
    return AccountDao.resetPassword(password)


@app.post("/account/login", tags=["Account"])
async def get_session(user: UserModel):
    return AccountDao.getSession(user)


@app.post("/account/delete/", tags=["Account"])
async def delete_account(id_account):
    return AccountDao.deleteAccountByID(id_account)


@app.post("/account/verify_account", tags=["Account"])
async def jwt_verify(token: str):
    return AccountDao.jwt_verify(token)

# Endpoint - Business


@app.get("/business", tags=["Business"])
async def get_all_business():
    return BusinessDao.getAllBusiness()


@app.get("/business/{uuid}", tags=["Business"])
async def get_business_by_id(uuid):
    return BusinessDao.getBusinessByID(uuid)


@app.post("/business/", tags=["Business"])
async def filter_by_business(business: BusinessModel):
    return BusinessDao.filterByBusiness(business)


@app.post("/business/create/", tags=["Business"])
async def create_business(business: NewBusinessModel):
    return BusinessDao.createBusiness(business)


@app.post("/business/update/", tags=["Business"])
async def update_business(business: BusinessModel):
    return BusinessDao.updateBusinessById(business)


@app.post("/business/delete/", tags=["Business"])
async def delete_business(id_business: str):
    return BusinessDao.deleteBusinessById(id_business)


@app.post("/business/customer/", tags=["Business"])
async def get_all_business_by_customer_id(customer_uuid):
    return BusinessDao.getBusinessByCustomerID(customer_uuid)

#Endpoint - Commessa

@app.get("/orders", tags=["Orders"])
async def get_all_orders():
    return OrderDao.getAllOrders()
@app.get("/orders/{uuid}", tags=["Orders"])
async def get_order_by_id(uuid):
    return OrderDao.getOrderByID(uuid)

@app.post("/orders/business/{uuid}", tags=["Orders"])
async def get_order_by_business_id(uuid):
    return OrderDao.getOrdersByBusinessId(uuid)

@app.post("/orders/create/", tags=["Orders"])
async def create_order(order: NewOrderModel):
    return OrderDao.createOrder(order)


@app.post("/orders/update/", tags=["Orders"])
async def update_order(order: OrderModel):
    return OrderDao.updateOrderById(order)


@app.post("/orders/delete/", tags=["Orders"])
async def delete_order(id_order: str):
    return OrderDao.deleteOrderByID(id_order)


@app.get("/orders/employee/{id_employee}", tags=["Orders"])
async def get_order_by_employee(id_employee):
    return OrderDao.getOrderByEmplyee(id_employee)


@app.post("/orders/customer", tags=["Orders"])
async def get_orders_by_customer_id_and_business_id(idcustomer_idbusiness: CustomerIDBusinessIDModel) -> dict:
    """ Send all orders of a customer """
    id_customer = idcustomer_idbusiness.id_customer
    id_business = idcustomer_idbusiness.id_business
    orders = OrderDao.getOrdersByCustomerIDAndBusinessID(
        id_customer, id_business)
    return orders

@app.post("/orders/employee/relational", tags=["Orders"])
async def add_employee_into_order(payload: OrderEmployeeModel):
    return OrderDao.addEmployeeIntoOrder(payload)

# Endpoint - Customer


@app.get("/customer", tags=["Customer"])
async def get_all_customer():
    return CustomerDao.getAllCustomers()


@app.post("/customer/business/{business_uuid}", tags=["Customer"])
async def get_all_customer_by_business_id(business_uuid):
    return CustomerDao.getCustomerByBusinessID(business_uuid)


@app.post("/customer/{uuid}", tags=["Customer"])
async def get_by_id(uuid):
    return CustomerDao.getCustomerByID(uuid)


@app.post("/customer/create/", tags=["Customer"])
async def create_customer(customer: NewCustomerModel):
    return CustomerDao.createCustomer(customer)


@app.post("/customer/delete/", tags=["Customer"])
async def delete_customer(id_customer: str):
    return CustomerDao.deleteCustomerByID(id_customer)


@app.post("/customer/update/", tags=["Customer"])
async def update_customer_by_id(customer: CustomerModel):
    return CustomerDao.updateCustomerByID(customer)


@app.get("/customer/{employeeID}", tags=["Customer"])
async def get_customer_name_by_employee_id(employeeID: str):
    return CustomerDao.getCustomerNameByEmployeeId(employeeID)

# Endpoint - Employee


@app.get("/employee", tags=["Employee"])
async def get_all_employees():
    return EmployeeDAO.getAllEmployees()


@app.get("/employee/all", tags=["Employee"])
async def get_all_employees_by_empty_key():
    return EmployeeDAO.getAllEmployeesByEmptyKey()


@app.post('/employee/', tags=["Employee"])
async def filter_by_employee(employee: NewEmployeeModel, idAzienda: str):
    return EmployeeDAO.filterByEmployee(employee, idAzienda)


@app.get("/employee/lastwork", tags=["Employee"])
async def get_employees_by_last_work():
    return EmployeeDAO.getEmployeesByLastWork()


@app.get("/employee/business/{id_business}", tags=["Employee"])
async def get_employees_by_business(id_business):
    return EmployeeDAO.getEmployeesByBusiness(id_business)


@app.get("/employee/account/{id_account}", tags=["Employee"])
async def get_employees_by_account(id_account):
    return EmployeeDAO.getEmployeesByAccount(id_account)


@app.get("/employee/{id_business}", tags=["Employee"])
async def get_employees_by_id(id_business):
    return EmployeeDAO.getEmployeesByID(id_business)


@app.get("/employee/order/{id_order}", tags=["Employee"])
async def get_employees_by_id_order(id_order):
    return EmployeeDAO.getEmployeeByIdOrder(id_order)


@app.post('/employee/create/', tags=["Employee"])
async def create_employee(employee: NewEmployeeModel):
    return EmployeeDAO.createEmployee(employee)


@app.post('/employee/update/', tags=["Employee"])
async def update_employee_by_id(employee: EmployeeModel):
    return EmployeeDAO.updateEmployeeByID(employee)


@app.post('/employee/delete/', tags=["Employee"])
async def delete_employee_by_id(id_employee: str):
    return EmployeeDAO.deleteEmployeeByID(id_employee)


@app.post('/employee/create/account', tags=["Employee"])
async def create_new_account_employee(payload: NewAccountEmployeeModel):
    return EmployeeDAO.createNewAccountEmployee(payload)


@app.get('/all/employees/account/business/{id_business}', tags=["Employee"])
async def show_all_Employees_by_Account_and_Business(id_business : str):
    return EmployeeDAO.getAllEmployeesAccountBusiness(id_business)


@app.get('/employee/{id_employee}/disabled', tags=["Employee"])
async def disable_account_by_Employee(id_employee: str):
    return EmployeeDAO.disableAccountByEmployeeID(id_employee)


@app.get('/employee/{id_employee}/enabled', tags=["Employee"])
async def enable_account_by_employee(id_employee: str):
    return EmployeeDAO.enableAccountByEmployeeID(id_employee)


@app.post('/employee/checkAccount', tags=["Employee"])
async def check_employee_account(id_dipendente: dict):
    """ Check if employee have is related to at least an account 
        :returns: {"ok": "ok"} if it does, else {"ok": "not"} """
    id_dipendente: str = id_dipendente["id_dipendente"]
    return EmployeeDAO.checkAccountByEmployee(id_dipendente)

@app.post('/employee/business/relational', tags=["Employee"])
async def add_employee_to_business(payload: EmployeeBusinessModel):
    return EmployeeDAO.insertEmployeeIntoBusiness(payload)

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

@app.get("/presences/business/{id_business}", tags=["Presence"])
async def get_all_presences_by_business(id_business : str):
    return PresenceDao.getPresencesByBusiness(id_business)

@app.get("/presence/all/first_name/last_name/{id_business}", tags=["Presence"])
async def get_all_presence_with_first_name_last_name(id_business : str):
    return PresenceDao.getAllPresenceWithFirstNameLastName(id_business)


@app.get("/presence/load_employee={id_employee}", tags=["Presence"])
async def get_presences_by_employee(id_employee: str):
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


@app.post("/presence/insertUpdate", tags=["Presence"])
async def insert_update_presence(payload: PresenceModel):
    return PresenceDao.insert_or_update_presence(payload)


@app.post("/presence/insertPresences", tags=["Presence"])
async def insert_presences(payload: List[NewPresenceModel]):
    return PresenceDao.insertPresences(payload)

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


@app.get("/order/employee/rate/", tags=["Order Employee"])
async def get_all_employee_by_customers_rate():
    return OrderEmployee.getAllEmployeeByCustomersRate()


@app.post("/order/employee/rate/", tags=["Order Employee"])
async def get_all_employee_by_customers_rate(params: graphPayloadModel):
    return OrderEmployee.getAllEmployeeByIdBusiness(params)


@app.post("/order/employee/create/", tags=["Order Employee"])
async def create_new_order_employee(params: NewOrderEmployee):
    return OrderEmployee.addOrderToEmployee(params)


@app.post("/order/employee/delete/", tags=["Order Employee"])
async def delete_order_employee(params: oem):
    return OrderEmployee.deleteOrderToEmployee(params)


@app.post("/order/employee/update/", tags=["Order Employee"])
async def update_order_employee(params: UpdateOrderEmployeeModel):
    return OrderEmployee.updateOrderToEmployee(params)