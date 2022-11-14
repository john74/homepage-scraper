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
    docstring
    """
    driver.get(f'{WEBSITE["url"]}/football/{country}/{league}/{WEBSITE["standings"]}/')
    return driver.find_elements(By.CSS_SELECTOR, WEBSITE['league_table'])


def get_league_standings(league_table):
    """
    docstring
    """

    league_standings = []
    for index, team in enumerate(league_table, start=1):
        rank = index
        name = team.find_element(By.CSS_SELECTOR, TEAM['name']).text
        status = team.find_element(By.CSS_SELECTOR, TEAM['status']).get_attribute('title')
        wins = team.find_element(By.CSS_SELECTOR, TEAM['wins']).text
        draws = team.find_element(By.CSS_SELECTOR, TEAM['draws']).text
        losses = team.find_element(By.CSS_SELECTOR, TEAM['losses']).text
        matches_played = int(wins) + int(draws) + int(losses)
        points = team.find_element(By.CSS_SELECTOR, TEAM['points']).text
        next_match_data = team.find_element(By.CSS_SELECTOR, TEAM['next_match_data'])
        next_match_data_list = next_match_data.get_attribute('title').split('\n')
        next_match_opponents_list = next_match_data_list[1].split(' - ')
        next_match_home_team = next_match_opponents_list[0]
        next_match_away_team = next_match_opponents_list[-1]
        next_match_date = next_match_data_list[-1]
        last_five_results = team.find_elements(By.CSS_SELECTOR, TEAM['last_five_results'])

        previous_results = []
        for result in last_five_results:
            result_data = result.get_attribute('title')
            previous_match_score = re.findall('(\\d+:\\d+)&', result_data)[0]
            previous_match_opponents = re.findall('\\((\\w+.+)\\)', result_data)[0]
            previous_match_date = re.findall('(\\d+\\..+)$', result_data)[0]
            previous_match_indicator = result.text
            previous_results.append([
                previous_match_score.strip(),
                previous_match_opponents.strip(),
                previous_match_date.strip(),
                previous_match_indicator.strip()
            ])

        league_standings.append({
            "rank": rank,
            "name": name.strip(),
            'status': status.strip(),
            'matches_played': str(matches_played).strip(),
            'wins': wins.strip(),
            'draws': draws.strip(),
            'losses': losses.strip(),
            'points': points.strip(),
            'next_match_home_team': next_match_home_team.strip(),
            'next_match_away_team': next_match_away_team.strip(),
            'next_match_date': next_match_date.strip(),
            'previous_results': previous_results
        })

    return league_standings
