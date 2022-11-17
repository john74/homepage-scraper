import os, re
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

def get_football_league_table(country, league):
    """
    Returns the table with the standings for all the football teams
    of the league
    """
    driver.get(f'{WEBSITE["url"]}/football/{country}/{league}/{WEBSITE["standings"]}/')
    return driver.find_elements(By.CSS_SELECTOR, WEBSITE['league_table'])

def get_team_standings(team):
    """
    Returns the standings for of a team
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
        "matches_played": int(wins) + int(draws) + int(losses),
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

def get_league_standings(league_table):
    """
    Returns the standings of all the teams of the league table
    """
    league_standings = []
    for rank, team in enumerate(league_table, start=1):
        team_standings = get_team_standings(team)
        team_standings['rank'] = rank
        team_standings['recent_results'] = get_recent_results(team)
        league_standings.append(team_standings)
    return league_standings
