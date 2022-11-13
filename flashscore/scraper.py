import os, re
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# from . variables import LEAGUES


service = Service(f'{os.getcwd()}/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

def get_league_table(sport, country, league):
    driver.get(f'https://www.flashscore.com/{sport}/{country}/{league}/standings/')
    return driver.find_elements(By.CSS_SELECTOR, '.ui-table__body > div')

def get_team_standings(team):
    pass
def get_standings(league_table):
    """
    docstring
    """

    team_standings = []
    for index, standing in enumerate(league_table):
        rank = index + 1
        team = standing.find_element(By.CSS_SELECTOR, '.tableCellParticipant__name').text
        promotion_or_relegation = standing.find_element(By.CSS_SELECTOR, '.tableCellRank').get_attribute('title')
        matches_played = standing.find_element(By.CSS_SELECTOR, ':nth-child(3)').text
        wins = standing.find_element(By.CSS_SELECTOR, ':nth-child(4)').text
        draws = standing.find_element(By.CSS_SELECTOR, ':nth-child(5)').text
        losses = standing.find_element(By.CSS_SELECTOR, ':nth-child(6)').text
        points = standing.find_element(By.CSS_SELECTOR, '.table__cell--points').text
        next_match_data = standing.find_element(By.CSS_SELECTOR, '.table__cell--form > :first-child').get_attribute('title').split('\n')
        next_match_opponents = next_match_data[1]
        next_match_date = next_match_data[-1]
        last_five_results = standing.find_elements(By.CSS_SELECTOR, '.table__cell--form > :not(:first-child)')

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

        team_standings.append({
            "rank": rank,
            "team": team.strip(),
            'promotion_or_relegation': promotion_or_relegation.strip(),
            'matches_played': matches_played.strip(),
            'wins': wins.strip(),
            'draws': draws.strip(),
            'losses': losses.strip(),
            'points': points.strip(),
            'next_match_opponents': next_match_opponents.strip(),
            'next_match_date': next_match_date.strip(),
            'previous_results': previous_results
        })

    return team_standings
# get_category_urls()
