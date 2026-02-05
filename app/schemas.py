from pydantic import BaseModel

class FilmCreate(BaseModel):
    title: str
    director: str