from fastapi import FastAPI, Depends, HTTPException
from .database import Base, engine, SessionLocal
from . import models
from sqlalchemy.orm import Session
from .schemas   import FilmCreate, FilmRead
from typing import List


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

@app.post("/films", response_model=FilmRead)
def create_film(film: FilmCreate, db: Session = Depends(get_db)):
    db_film = models.Film(
        title=film.title,
        director=film.director
    )
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

@app.get("/films", response_model=List[FilmRead])
def get_films(db: Session = Depends(get_db)):
    return db.query(models.Film).all()

@app.delete("/films/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(models.Film).filter(models.Film.id == film_id).first()

    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")

    db.delete(film)
    db.commit()
    return {"ok": True, "deleted_id": film_id}