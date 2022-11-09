from datetime import datetime, date
from fastapi import APIRouter

from . import scraper
router = APIRouter()

async def get_articles(names):
    """ Returns a list of articles for a specific team or competition"""
    articles = []
    titles = []
    rejected_titles_substrings = [": η βαθμολογία "]
    today = datetime.strptime(date.today().strftime('%d.%m.%Y'), '%d.%m.%Y')
    for name in names:
        article = scraper.get_article(f'football/{name}')
        title = article['title'].lower()
        is_unique = title not in titles
        days_since_post = (today - datetime.strptime(article['date'], '%d.%m.%Y')).days
        is_at_most_a_week = days_since_post <= 7
        title_is_accepted = any(substring not in title for substring in rejected_titles_substrings)

        if is_unique and is_at_most_a_week and title_is_accepted:
            titles.append(title)
            articles.append(article)
    return articles

@router.get("/api/sports/greek/football/competitions/articles")
async def fetch_greek_football_competitions_articles():
    """
    Returns the articles of all available greek football
    competitions in sport24.gr
    """
    names = scraper.get_greek_competitions_names()
    return await get_articles(names)

@router.get("/api/sports/international/football/competitions/articles")
async def fetch_international_football_competitions_articles():
    """
    Returns the articles of all available international football
    competitions in sport24.gr
    """
    names = scraper.get_international_competitions_names()
    return await get_articles(names)

@router.get("/api/sports/greek/football/teams/articles")
async def fetch_greek_football_teams_articles():
    """
    Returns the articles of all available greek football
    teams in sport24.gr
    """
    names = scraper.get_greek_team_names()
    return await get_articles(names)

@router.get("/api/sports/international/football/teams/articles")
async def fetch_international_football_teams_articles():
    """
    Returns the articles of all available international football
    teams in sport24.gr
    """
    names = scraper.get_international_team_names()
    return await get_articles(names)
