from pydantic import BaseModel


class ArticleBase(BaseModel):
    id: int
    url: str
    author: str
    date: str
    time: str
    small_image: str
    medium_image: str
    large_image: str
    title: str
    body: str
