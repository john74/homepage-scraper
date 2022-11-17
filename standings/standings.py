from fastapi import APIRouter

from . import scraper

router = APIRouter()

@router.get("/api/football-standings/")
def get_football_standings(country, league):
    """
    Returns the standings of all the football teams
    that compete at the league specified by the country
    and league parameters
    """
    league_table = scraper.get_football_league_tables(country, league)
    return scraper.get_league_standings(league_table)
