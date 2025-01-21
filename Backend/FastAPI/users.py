from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#inicia el server -> uvicorn users:app --reload
class User(BaseModel):
  name: str
  surname: str
  url: str
  age: int

users = [User("Brais", "Moure", "https://moure.dev", 35)]
  

@app.get("/usersjson")
async def usersjson():
  return [{"name":"jesus", "surname":"zamora", "url":"https://jesuszamora.com", "age":23},
          {"name":"daniel", "surname":"santamaria", "url":"https://danielzam.com", "age":15},
          {"name":"santiago", "surname":"zamora", "url":"https://santizam.com", "age":16}]
  
@app.get("/usersclass")
async def usersclass():
  return User(name = "Jesus", surname = "Zamora", url = "https://jesuszamora.com", age = 23)

#minuto 2:02:50
