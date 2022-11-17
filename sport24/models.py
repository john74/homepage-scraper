from pydantic import BaseModel


class Article(BaseModel):
    url: str
    author: str
    date: str
    time: str
    small_image: str
    medium_image: str
    large_image: str
    title: str
    body: str
