from fastapi import FastAPI
from .database import Base, engine
from . import models

Base.metadata.create_all(bind=engine)

#import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Films API is running"}