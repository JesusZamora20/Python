from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return "Hi FastAPI"


@app.get("/url")
async def urk():
  return{"url" : "https://python.org"}
  
#Iniciar el server -> uvicorn main:app --reload
#Detener el server: ctrl + c

#documentacion con swagger -> localhost/docs
#documentacion con redocly -> localhost/redoc

#operacion get
#Download postman <- delete when downloaded


