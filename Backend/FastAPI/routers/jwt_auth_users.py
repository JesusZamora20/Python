from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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
    "email": "jesusbermudez@mourede.com",
    "disabled": False,
    "password": "123456"
  },
  "yolandalozano": {
    "username": "yolandalozano",
    "full_name": "yolanda yunuliexis",
    "email": "yolita@lozano.com",
    "disabled": True,
    "password": "654321"
  }
}
