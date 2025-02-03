from fastapi import FastAPI
from routers import users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# routers
app.include_router(users_db.router)

app.mount(("/static"), StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return "Hi FastAPI"

@app.get("/url")
async def url():
    return {"url": "https://python.org"}
