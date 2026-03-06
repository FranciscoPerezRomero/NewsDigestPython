from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List
from db.database import create_User, add_userTags, get_user_tags, get_all_users, init_db
from main import send_daily_digest
#* Instancia de FastApi
app = FastAPI()

#*Configuracion de CORS|
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica solo los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#* Se inicia la base de datos
init_db()
#* Modelo para validación automatica
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    tags: List[str]

@app.get("/")
def root():
    return {"message":"NewsDigest API is running"}


@app.post("/register")
def register_user(user:UserRegister):
    if len(user.tags) >= 1 and len(user.tags) <= 3:
        userId = create_User(user.name,user.email)
        if userId is None:
            raise HTTPException(status_code=400, detail="Email ya registrado")
        else:
            add_userTags(userId,user.tags)
            return {"message":"Usuario registrado exitosamente","userId":userId}
    else:
        raise HTTPException(status_code=400, detail="Cantidad de tags invalido")
    pass

@app.get("/send-digest")
def send_digest():
    count = send_daily_digest()
    return {"message":"Process Success -> ", "users_processed":{count}}