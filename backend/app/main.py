from fastapi import FastAPI
from app.core.db import create_db_and_tables
from app.api.main import api_router



app = FastAPI()


app.include_router(api_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
def home():
    return {"Ok": "Application starts"}