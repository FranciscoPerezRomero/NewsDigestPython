from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from db.database import create_User, add_userTags, get_user_tags, get_all_users

#* Instancia de FastApi
app = FastAPI()

#* Modelo para validación automatica
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    tags: List[str]

