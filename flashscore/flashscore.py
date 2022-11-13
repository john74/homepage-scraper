from fastapi import APIRouter

from . import scraper
from . variables import QUERY_PARAMETERS
router = APIRouter()

@router.get("/api/sport-standings/")
async def get_sport_standings(sport, country, league):
    """
    docstring
    """
    pass
    # category_urls = scraper.get_category_urls(QUERY_PARAMETERS[category])
    # return await scraper.get_articles(category_urls)
