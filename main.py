from uuid import uuid4
from typing import List
from fastapi import FastAPI

from models import Article
from scraper import get_sport24_greek_sports_articles
# run server as uvicorn main:app --port 8086  --reload
app = FastAPI()
articles: List[Article] = [
  # articles database of type List. The list is of type Article
  # Article(
  #   website = "sport24",
  #   author = "Article 1",
  #   post_date = "05.11.2022",
  #   post_time = "18:51",
  #   article_title = "Lorem ipsum dolor sit ammet",
  #   article_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
  #   article_img_link = "https://images.pexels.com/photos/14181566/pexels-photo-14181566.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  #   article_small_img_link = "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
  # ),
  #   Article(
  #   website = "sport24",
  #   author = "Article 2",
  #   post_date = "05.11.2022",
  #   post_time = "18:51",
  #   article_title = "Lorem ipsum dolor sit ammet",
  #   article_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
  #   article_img_link = "https://images.pexels.com/photos/14181566/pexels-photo-14181566.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  #   article_small_img_link = "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
  # )
]

@app.get("/api/sports/articles/greek")
async def fetch_sports_articles():
  """ Returns the contents of the sports articles """
  teams = ['panathinaikos', 'olympiacos', 'aek', 'paok', 'aris']
  return get_sport24_greek_sports_articles(teams)

@app.post("/api/sports/articles/greek")
async def register_sports_article(article: Article):
  """
  Adds and article of type Article to the articles database.
  Returns the article titles
  """
  articles.append(article)
  return {"article_title": article.article_title}
