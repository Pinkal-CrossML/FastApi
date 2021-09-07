from fastapi import FastAPI, Depends, Response, status, HTTPException
from . import schemas, models
from . database import engine, get_db, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .routers import blog, user, login



app = FastAPI()

 
models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)
