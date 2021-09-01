from typing import Optional, List

from pydantic import BaseModel


class Data(BaseModel):
    q: Optional[str] = 'War'


class Thumbnail(BaseModel):
    thumbnail: str


class BookByID(BaseModel):
    title: str
    authors: Optional[List[str]] = ''
    publishedDate: Optional[str] = ''
    categories: Optional[List[str]] = ''
    averageRating: Optional[int] = ''
    ratingsCount: Optional[int] = ''
    imageLinks: Optional[Thumbnail] = ''
