# from datetime import datetime, date
from fastapi import APIRouter

from . import scraper, variables
router = APIRouter()

@router.get("/api/greek-football-articles")
async def fetch_greek_football_articles():
    """
    Returns the articles from football > Greece > <category>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.GREEK_FOOTBALL_SELECTOR)
    return await scraper.get_articles(category_urls)

@router.get("/api/international-football-articles")
async def fetch_international_football_articles():
    """
    Returns the articles from football > International > <category>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.INTERNATIONAL_FOOTBALL_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/greek-football-teams-articles")
async def fetch_greek_football_teams_articles():
    """
    Returns the articles from football > Greek teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.GREEK_FOOTBALL_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/international-football-teams-articles")
async def fetch_international_football_teams_articles():
    """
    Returns the articles from football > top teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.INTERNATIONAL_FOOTBALL_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/greek-basketball-teams-articles")
async def fetch_greek_basketball_teams_articles():
    """
    Returns the articles from basketball > Greek teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.GREEK_BASKETBALL_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/euroleague-articles")
async def fetch_euroleague_articles():
    """
    Returns the articles from basketball > Euroleague teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.EUROLEAGUE_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/nba-articles")
async def fetch_nba_articles():
    """
    Returns the articles from basketball > NBA teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.NBA_TEAMS_SELECTOR)
    return await get_articles(category_urls)
