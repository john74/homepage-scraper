from fastapi import APIRouter

from . import scraper
router = APIRouter()

async def get_sport24_articles(names):
    """ Returns a list of articles for a specific team or competition"""
    articles = []
    titles = []
    today = datetime.strptime(date.today().strftime('%d.%m.%Y'), '%d.%m.%Y')
    for name in names:
        article = sport24.get_article(f'football/{name}')
        is_unique = article['title'] not in titles
        days_since_post = (today - datetime.strptime(article['date'], '%d.%m.%Y')).days
        is_at_most_a_week = days_since_post <= 7

        if is_unique and is_at_most_a_week:
            titles.append(article['title'])
            articles.append(article)
    return articles

@router.get("/api/sports/greek/football/competitions/articles")
async def fetch_greek_football_competitions_articles():
    """
    Returns the articles of all available greek football
    competitions in sport24.gr
    """
    names = scraper.get_greek_competitions_names()
    return await get_sport24_articles(names)

@router.get("/api/sports/international/football/competitions/articles")
async def fetch_international_football_competitions_articles():
    """
    Returns the articles of all available international football
    competitions in sport24.gr
    """
    names = scraper.get_international_competitions_names()
    return await get_sport24_articles(names)

@router.get("/api/sports/greek/football/teams/articles")
async def fetch_greek_football_teams_articles():
    """
    Returns the articles of all available greek football
    teams in sport24.gr
    """
    names = scraper.get_greek_team_names()
    return await get_sport24_articles(names)

@router.get("/api/sports/international/football/teams/articles")
async def fetch_international_football_teams_articles():
    """
    Returns the articles of all available international football
    teams in sport24.gr
    """
    names = scraper.get_international_team_names()
    return await get_sport24_articles(names)
