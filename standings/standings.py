from fastapi import APIRouter

from . import scraper

router = APIRouter()

@router.get("/api/football-standings/")
def get_football_standings(country, league):
    """
    docstring
    """
    league_table = scraper.get_football_league_table(country, league)
    return scraper.get_league_standings(league_table)
