from fastapi import FastAPI
from routers import products, users,basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()


#routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount(("/static"), StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
  return "Hi FastAPI"


@app.get("/url")
async def url():
  return{"url" : "https://python.org"}
  
#Iniciar el server -> uvicorn main:app --reload
#Detener el server: ctrl + c

#documentacion con swagger -> localhost/docs
#documentacion con redocly -> localhost/redoc

#operacion get
#Download postman <- delete when downloaded


