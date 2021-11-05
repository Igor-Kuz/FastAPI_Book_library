from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int


class BookOut(Book):
    id: int


class Author(BaseModel):
    first_name: str = Field(..., max_length= 31)
    last_name: str = Field(..., min_length= 3)
    age: int = Field(..., gt=14, lt=90, description="Author shouldn`t be younger than 15 and older than 90")

   # @validator('age')
    # def check_age(cls, v):
    #    if v < 14 > 90:
    #        raise ValueError('Author age must be more than 14')
    #    return v