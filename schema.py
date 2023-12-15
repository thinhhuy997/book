# schema.py

from typing import Optional
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    description: str

class Book(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
