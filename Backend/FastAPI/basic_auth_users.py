#OAuth2
  
#new file -. basic_auth_users.py
#run uvicorn basic_auth_users:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool  

users_db = {
  "jesus": {
    "username": "jesusinho",
    "full_name": "jesus Do Santos",
    "email": "jesusdossantos@gmail.com",
    "disabled": False,
    "password": "123456"
  },
  "Yolanda": {
    "username": "Yolandayro",
    "full_name": "Yolanda Isabel",
    "email": "Yolandita@gmail.com",
    "disabled": True,
    "password": "56789"
  },
}

#4:12
