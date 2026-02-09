from pydantic import BaseModel, ConfigDict

class FilmCreate(BaseModel):
    title: str
    director: str
class FilmRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Pydantic v2
    id: int
    title: str
    director: str