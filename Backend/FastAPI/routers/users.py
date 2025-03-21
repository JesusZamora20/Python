from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

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
  

@router.get("/usersjson")
async def usersjson():
  return [{"name":"jesus", "surname":"zamora", "url":"https://jesuszamora.com", "age":23},
          {"name":"daniel", "surname":"santamaria", "url":"https://danielzam.com", "age":15},
          {"name":"santiago", "surname":"zamora", "url":"https://santizam.com", "age":16}]
  
@router.get("/users")
async def users():
  return users_list

#path
@router.get("/user/{id}")
async def user(id: int):
  return search_user(id)

#query /?id=1&name=hola
@router.get("/user/")
async def user(id: int):
  return search_user(id)

#post  

@router.post("/user/", status_code=201)
async def user(user: User):
  if type(search_user(user.id)) == User:
    #return {"Error": "User already exists"}
    raise HTTPException(status_code=204, detail="User already exists")
  else:
      users_list.append(user)
      return user

#put
@router.put("/user/")
async def user(user: User):
  found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      found = True

  if not found:
    return {"Error": "User not updated"}
  else:
    return user

#delete
@router.delete("/user/{id}")
async def user(id: int):
  found = False
  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]
      found = True
    
  if not found:
    return {"Error": "User not found"}

def search_user(id: int):
  try: 
    for user in users_list:
      if user.id == id:
        return user
    return None
  except:
    return {"error":"User not found"}