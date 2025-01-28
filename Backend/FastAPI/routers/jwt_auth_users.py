from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

#--------------------------------------------
ALGORITHM = "HS256"

ACCESS_TOKEN_DURATION = 1

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])
#-------------------------------------

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool


class UserDB(User):
  password: str


users_db = {
  "jesusdavid": {
    "username": "jesusdavid",
    "full_name": "jesus bermudez",
    "email": "jesusbermudez@dev.com",
    "disabled": False,
    "password": "$2a$12$13paE8zJOzfppwtmuCrjkOQ7IQMf8a4uik9FHi4rTfaCOftJeMTu2"
  },
  "yolandalozano": {
    "username": "yolandalozano",
    "full_name": "yolanda Lozano",
    "email": "yolita@lozano.com",
    "disabled": True,
    "password": "$2a$12$q5OOd2cNgT9fctphBRJBNuPFCs3URsHf51JFlwXbJmdb05tcTyQjC"
  }
}

# install python-jose
#pip install "python-jose[cryptography]"
#pip install "passlib[bcrypt]"

def search_user_db(username: str):
  if username in users_db:
    return UserDB(**users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
  user_db = users_db.get(form.username)
  if not user_db:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail="El usuario no es correcto")

  user = search_user_db(form.username)

  crypt.verify(form.password, user.password)
  if not crypt.verify(form.password, user.password):
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail="La contraseña no es correcta")
    
  expire = datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_DURATION)

  
  
  return {"access_token": user.username, "token_type": "bearer"}












