from fastapi import APIRouter, HTTPException, status
from Backend.FastAPI.MongoDBConnection.db.models.user import User
from Backend.FastAPI.MongoDBConnection.db.schemas.user import user_schema
from Backend.FastAPI.MongoDBConnection.db.client import db_client

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses = {status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

users_list = []
 
@router.get("/")
async def users():
  return users_list

#path
@router.get("/{id}")
async def user(id: int):
  return search_user(id)

#query /?id=1&name=hola
@router.get("/")
async def user(id: int):
  return search_user(id)


#post  
@router.post("/",response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
  #if type(search_user(user.id)) == User:
    #return {"Error": "User already exists"}
    #raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User already exists")
  
  user_dict = dict(user)
  del user_dict["id"]

  id = db_client.local.users.insert_one(user_dict).inserted_id

  new_user = user_schema(db_client.local.users.find_one({"_id": id}))

  return User(**new_user)


#put
@router.put("/")
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
@router.delete("/{id}")
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