from datetime import datetime, date
from uuid import uuid4
from typing import List
from fastapi import FastAPI

from models import Article
import sport24_scraper as sport24
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


async def get_sport24_articles(names):
    """ Returns a list of articles for a specific team or competition"""
    articles = []
    titles = []
    today = datetime.strptime(date.today().strftime('%d.%m.%Y'), '%d.%m.%Y')
    for name in names:
        article = sport24.get_sport24_article(f'football/{name}')
        is_unique = article['title'] not in titles
        days_since_post = (today - datetime.strptime(article['date'], '%d.%m.%Y')).days
        is_at_most_a_week = days_since_post <= 7

        if is_unique and is_at_most_a_week:
            titles.append(article['title'])
            articles.append(article)
    return articles

@app.get("/api/sports/greek/football/competitions/articles")
async def fetch_greek_football_competitions_articles():
    """
    Returns the articles of all available greek football
    competitions in sport24.gr
    """
    names = sport24.get_sport24_greek_competitions_names()
    return await get_sport24_articles(names)

@app.get("/api/sports/international/football/competitions/articles")
async def fetch_international_football_competitions_articles():
    """
    Returns the articles of all available international football
    competitions in sport24.gr
    """
    names = sport24.get_sport24_international_competitions_names()
    return await get_sport24_articles(names)

@app.get("/api/sports/greek/football/teams/articles")
async def fetch_greek_football_teams_articles():
    """
    Returns the articles of all available greek football
    teams in sport24.gr
    """
    names = sport24.get_sport24_greek_team_names()
    return await get_sport24_articles(names)

@app.get("/api/sports/international/football/teams/articles")
async def fetch_international_football_teams_articles():
    """
    Returns the articles of all available international football
    teams in sport24.gr
    """
    names = sport24.get_sport24_international_team_names()
    return await get_sport24_articles(names)
