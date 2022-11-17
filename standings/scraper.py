import os, re
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from . variables import WEBSITE, TEAM

service = Service(f'{os.getcwd()}/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

def get_football_league_tables(country, league):
    """
    Returns all the available tables of the league
    """
    driver.get(f'{WEBSITE["football_url"]}/{country}/{league}')

    try:
        league_season = driver.find_element(By.CSS_SELECTOR, WEBSITE['league_season']).text
    except Exception:
        return

    league_season_year = int(league_season.split('/')[0])
    current_year = int(date.today().strftime('%Y'))
    table_is_updated = (current_year == league_season_year) or \
                       (current_year + 1 == league_season_year)

    if table_is_updated:
        return driver.find_elements(By.CSS_SELECTOR, WEBSITE['league_tables'])
    return

def get_team_standings(team):
    """
    Returns all the available info about a team in the league table
    """
    wins = team.find_element(By.CSS_SELECTOR, TEAM['wins']).text
    draws = team.find_element(By.CSS_SELECTOR, TEAM['draws']).text
    losses = team.find_element(By.CSS_SELECTOR, TEAM['losses']).text
    next_match_data = team.find_element(By.CSS_SELECTOR, TEAM['next_match_data'])
    next_match_data_list = next_match_data.get_attribute('title').split('\n')
    next_match_opponents_list = next_match_data_list[1].split(' - ')

    return {
        "name": team.find_element(By.CSS_SELECTOR, TEAM['name']).text,
        "status": team.find_element(By.CSS_SELECTOR, TEAM['status']).get_attribute('title'),
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "matches_played": str(int(wins) + int(draws) + int(losses)),
        "points": team.find_element(By.CSS_SELECTOR, TEAM['points']).text,
        "next_match_home_team": next_match_opponents_list[0],
        "next_match_away_team": next_match_opponents_list[-1],
        "next_match_date": next_match_data_list[-1]
    }

def get_recent_results(team):
    """
    Returns the most recent past results of a team
    """
    recent_results = team.find_elements(By.CSS_SELECTOR, TEAM['recent_results'])
    results = []
    for result in recent_results:
        data = result.get_attribute('title')
        match_score = re.findall(TEAM['match_score'], data)[0]
        match_opponents = re.findall(TEAM['match_opponents'], data)[0]
        match_date = re.findall(TEAM['match_date'], data)[0]
        result_letter_indicator = result.text
        results.append([
            match_score.strip(),
            match_opponents.strip(),
            match_date.strip(),
            result_letter_indicator.strip()
        ])
    return results

def get_league_standings(league_tables):
    """
    Returns the standings of all the teams of all
    the league tables
    """
    if league_tables is None:
        return
    league_standings = []
    for group, table in enumerate(league_tables):
        table_standings = []
        teams = table.find_elements(By.CSS_SELECTOR, WEBSITE['league_teams'])
        for rank, team in enumerate(teams, start=1):
            team_standings = get_team_standings(team)
            team_standings['rank'] = rank
            team_standings['recent_results'] = get_recent_results(team)
            table_standings.append(team_standings)
        league_standings.append({group:table_standings})
    return league_standings
