from fastapi import APIRouter

from . import scraper

router = APIRouter()

@router.get("/api/sport-standings/")
def get_sport_standings(sport, country, league):
    """
    docstring
    """
    # if sport.lower() == 'basketball':
    #     league = FOOTBALL_LEAGUES[country]
    # else:
    #     league = BASKETBALL_LEAGUES[country]
    league_table = scraper.get_league_table(sport, country, league)
    return scraper.get_league_standings(league_table)
