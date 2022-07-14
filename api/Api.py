from fastapi.middleware.cors import CORSMiddleware
# from Dao.TipoPresenzaDao import TipoPresenzaDao
from Dao.TipoAccountDao import TipoAccountDao
from api.Dao.BusinessDao import BusinessDao
from api.Dao.AccountDao import AccountDao
from Dao.PresenceDao import PresenceDao
from Dao.BusinessDao import BusinessDao
from Dao.CustomerDao import CustomerDao
from Dao.EmployeeDAO import EmployeeDAO
from Dao.AccountDao import AccountDao
# from Dao.OrderDAO import OrderDao
from fastapi import FastAPI

from api.Dao.CustomerDao import CustomerDao

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
 
@app.get("/employee")
async def getAllEmployees():
    return EmployeeDAO.getAllEmployees()

@app.get("/employee/{id}")
async def get_Employees_By_ID(id):
    return EmployeeDAO.getEmployeesByID(id)

 
@app.get("/customer")
async def getAllCustomer():
    return CustomerDao.getAllCustomers()

@app.get("/business")
async def getAllBusiness():
    return BusinessDao.getAllBusiness()

@app.get("/account")
async def getAllAccounts():
    return AccountDao.getAllAccounts()

# @app.get("/order")
# async def getAllOrders():
#     return OrderDao.getAllOrders()
    
@app.get("/presence")
async def getAllPresence():
    return PresenceDao.getAllPresence()



# Endpoint - TipoAccount
@app.get("/tipo/account")
async def get_all_tipo_account():
    return TipoAccountDao.getAllTipoAccount()

@app.get("/nome/account/{id_account}")
async def get_tipo_account_by_id(id_account):
    return TipoAccountDao.getTipoAccountByNomeTipoAccount(id_account)





# @app.get("/random")
# async def get_random_question():
#     return QuestionDao.getRandomQuestion()

# @app.get("/answer/{question_id}")
# async def get_answer_by_question_id(question_id ):
#    return AnswerDao.getAnswerByQuestionId(question_id)

# @app.get("/score")
# async def get_all_score():
#    return TestResultDao.getAllScores()

# @app.get("/highscore")
# async def get_highest_score():
#    return TestResultDao.getHighScore()

# @app.get("/user")
# async def get_all_users():
#     return UserDao.getAllUsers()
    
# @app.get("/user/{username}/{password}")
# async def get_user(username,password):
#     return UserDao.getUserByIdAndPassword(username,password)