from pydantic import BaseModel


class ArticleSchema(BaseModel):
    id: int
    website = str
    main_category = str
    category = str
    url: str
    author: str
    post_date: str
    post_time: str
    images: str
    title: str
    body: str
