from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#inicia el server -> uvicorn users:app --reload
class User(BaseModel):
  id: int
  name: str
  surname: str
  url: str
  age: int

users_list = [User(id=1,name="Brais",surname= "Moure", url="https://moure.dev", age=35),
         User(id=2,name="jesus", surname="zamora", url="https://moure.dev", age=23),
         User(id=3,name="yolanda", surname="lozano", url="https://moure.dev", age=25)]
  

@app.get("/usersjson")
async def usersjson():
  return [{"name":"jesus", "surname":"zamora", "url":"https://jesuszamora.com", "age":23},
          {"name":"daniel", "surname":"santamaria", "url":"https://danielzam.com", "age":15},
          {"name":"santiago", "surname":"zamora", "url":"https://santizam.com", "age":16}]
  
@app.get("/users")
async def users():
  return users_list

#path
@app.get("/user/{id}")
async def user(id: int):
  return search_user(id)

#query
@app.get("/user/")
async def user(id: int):
  return search_user(id)


def search_user(id: int):
  try: 
    for user in users_list:
      if user.id == id:
        return user
    return None
  except:
    return {"error":"User not found"}