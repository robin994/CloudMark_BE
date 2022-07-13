from fastapi.middleware.cors import CORSMiddleware
from Dao.TipoPresenzaDao import TipoPresenzaDao
from Dao.TipoAccountDao import TipoAccountDao
from Dao.PresenceDao import PresenceDao
from Dao.BusinessDao import BusinessDao
from Dao.CustomerDao import CustomerDao
from Dao.EmployeeDAO import EmployeeDAO
from Dao.AccountDao import AccountDao
from Dao.OrderDAO import OrderDao
from fastapi import FastAPI

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
 
@app.get("/question")
async def get_all_questions():
    return QuestionDao.getAllQuestion()
 
@app.get("/question/{id_questions}")
async def get_question_by_question_id(id_questions):
    return QuestionDao.getQuestionById(id_questions)
    
@app.get("/random")
async def get_random_question():
    return QuestionDao.getRandomQuestion()

@app.get("/answer/{question_id}")
async def get_answer_by_question_id(question_id ):
   return AnswerDao.getAnswerByQuestionId(question_id)

@app.get("/score")
async def get_all_score():
   return TestResultDao.getAllScores()

@app.get("/highscore")
async def get_highest_score():
   return TestResultDao.getHighScore()

@app.get("/user")
async def get_all_users():
    return UserDao.getAllUsers()
    
@app.get("/user/{username}/{password}")
async def get_user(username,password):
    return UserDao.getUserByIdAndPassword(username,password)