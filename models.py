from pydantic import BaseModel

class Article(BaseModel):
  """
  A class to represent the Article model.
  """
  website: str 
  author: str
  post_date: str
  post_time: str
  article_title: str
  article_body: str
  article_img_link: str
  article_small_img_link: str
