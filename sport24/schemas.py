from pydantic import BaseModel


class ArticleBase(BaseModel):
    id: int
    website = str
    category = str
    general_category = str
    url: str
    author: str
    date: str
    time: str
    images: str
    title: str
    body: str
