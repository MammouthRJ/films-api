from fastapi import FastAPI, Depends
from .database import Base, engine, SessionLocal
from . import models
from sqlalchemy.orm import Session
from .schemas   import FilmCreate


Base.metadata.create_all(bind=engine)

#import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Films API is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/films")
def create_film(film: FilmCreate, db: Session = Depends(get_db)):
    db_film = models.Film(
        title=film.title,
        director=film.director
    )
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

@app.get("/films")
def get_films(db: Session = Depends(get_db)):
    return db.query(models.Film).all()