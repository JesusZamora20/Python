from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

# install python-jose
#pip install "python-jose[cryptography]"
#pip install "passlib[bcrypt]"
#5:38:32

#--------------------------------------------
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "15f85a18b08c9fc377d83e44f9a39688640dbdf0f7f452b39126f43bbd4018f5"
router = APIRouter()

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



def search_user_db(username: str):
  if username in users_db:
    return UserDB(**users_db[username])

def search_user(username: str):
  if username in users_db:
    return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
  exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Credenciales de autenticación inválidas",
      headers={"WWW-Authenticate": "Bearer"})  

  try:
    username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
    if username is None:
      raise exception

  except JWTError:
    raise exception

  return search_user(username)




async def current_user(user: User = Depends(auth_user)):
  
  if user.disabled:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Usuario deshabilitado")

  return user


@router.post("/login")
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
      detail="La password no es correcta")
    

  access_token = {
    "sub": user.username,
    "exp": datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_DURATION)
  }
  
  return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

 
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
  return user








