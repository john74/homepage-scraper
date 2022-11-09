from datetime import datetime, date
from fastapi import APIRouter

from . import scraper, variables
router = APIRouter()

async def get_articles(names):
    """
    Returns a list of articles. An article is accepted
    if it is unique, not older than a week and the title
    doesn't contain a substring from rejected_titles_substrings
    """
    articles = []
    titles = []
    rejected_titles_substrings = [
        ": Η βαθμολογία ", "Αθλητικές μεταδόσεις:"
    ]

    today = datetime.strptime(date.today().strftime('%d.%m.%Y'), '%d.%m.%Y')
    for name in names:
        article = scraper.get_article(f'football/{name}')
        if article is None:
            continue
        title = article['title']
        is_unique = title not in titles
        days_since_post = (today - datetime.strptime(article['date'], '%d.%m.%Y')).days
        is_at_most_a_week = days_since_post <= 7

        title_is_accepted = True
        for substring in rejected_titles_substrings:
            if substring.lower() in title.lower():
                title_is_accepted = False
                break

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
    names = scraper.get_category_names(variables.GREEK_COMPETITIONS_SELECTOR)
    return await get_articles(names)

@router.get("/api/sports/international/football/competitions/articles")
async def fetch_international_football_competitions_articles():
    """
    Returns the articles of all available international football
    competitions in sport24.gr
    """
    names = scraper.get_category_names(variables.INTERNATIONAL_COMPETITIONS_SELECTOR)
    return await get_articles(names)

@router.get("/api/sports/greek/football/teams/articles")
async def fetch_greek_football_teams_articles():
    """
    Returns the articles of all available greek football
    teams in sport24.gr
    """
    names = scraper.get_category_names(variables.GREEK_TEAMS_SELECTOR)
    return await get_articles(names)

@router.get("/api/sports/international/football/teams/articles")
async def fetch_international_football_teams_articles():
    """
    Returns the articles of all available international football
    teams in sport24.gr
    """
    names = scraper.get_category_names(variables.INTERNATIONAL_TEAMS_SELECTOR)
    return await get_articles(names)
