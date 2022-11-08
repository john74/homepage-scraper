from uuid import uuid4
from typing import List
from fastapi import FastAPI

from models import Article
from scraper import get_sport24_article, get_sport24_greek_team_names, get_sport24_international_team_names
# run server as uvicorn main:app --port 8086  --reload
app = FastAPI()
articles_db: List[Article] = [
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

@app.get("/api/sports/greek/football")
async def fetch_greek_football():
    pass

@app.get("/api/sports/greek/football/articles")
async def fetch_greek_football_articles():
    """ Returns the contents of the article """
    articles = []
    titles = []
    for team in get_sport24_greek_team_names():
        article = get_sport24_article(f'football/{team}')
        # Teams can share an article. If that's the case don't include it
        if article['title'] not in titles:
            titles.append(article['title'])
            articles.append(article)
    return articles

@app.get("/api/sports/international/football/articles")
async def fetch_international_football_articles():
    """ Returns the contents of the article """
    articles = []
    titles = []
    for team in get_sport24_international_team_names():
        article = get_sport24_article(f'football/{team}')
        # Teams can share an article. If that's the case don't include it
        if article['title'] not in titles:
            titles.append(article['title'])
            articles.append(article)
    return articles
