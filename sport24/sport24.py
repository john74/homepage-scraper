# from datetime import datetime, date
from fastapi import APIRouter

from . import scraper
from . variables import QUERY_PARAMETERS
router = APIRouter()

@router.get("/api/sport24-articles/")
async def get_sport24_articles(category):
    """
    Returns the articles from football > Greece > <category>
    navbar menu
    """
    category_urls = scraper.get_category_urls(QUERY_PARAMETERS[category])
    return await scraper.get_articles(category_urls)
    """
    Returns the articles from basketball > NBA teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.NBA_TEAMS_SELECTOR)
    return await get_articles(category_urls)
