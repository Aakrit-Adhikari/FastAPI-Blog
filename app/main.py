from fastapi import FastAPI
from . import models, Schemas # Notice the dot and the Capital S
from .db import engine        # You renamed database.py to db.py
from .routers import posts
from app.routers import posts

app=FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(posts.router)

    
