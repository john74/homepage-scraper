from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class Article(BaseModel):
  id: Optional[UUID] = uuid4
  author: Optional[str] = str
  post_date: Optional[str] = str
  post_time: Optional[str] = str
  article_text: str
  article_img_link: Optional[str] = str
  article_small_img_link: Optional[str] = str
