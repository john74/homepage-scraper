import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import sport24_variables as sport24

service = Service(f'{os.getcwd()}/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

def get_sport24_greek_competitions_names():
    driver.get(sport24.BASE_URL)
    competitions = driver.find_elements(By.CSS_SELECTOR, sport24.GREEK_COMPETITIONS_SELECTOR)
    names = []
    for competition in competitions:
        href = competition.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_sport24_international_competitions_names():
    driver.get(sport24.BASE_URL)
    competitions = driver.find_elements(By.CSS_SELECTOR, sport24.INTERNATIONAL_COMPETITIONS_SELECTOR)
    names = []
    for competition in competitions:
        href = competition.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_sport24_greek_team_names():
    driver.get(sport24.BASE_URL)
    teams = driver.find_elements(By.CSS_SELECTOR, sport24.GREEK_TEAMS_SELECTOR)
    names = []
    for team in teams:
        href = team.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_sport24_international_team_names():
    driver.get(sport24.BASE_URL)
    teams = driver.find_elements(By.CSS_SELECTOR, sport24.INTERNATIONAL_TEAMS_SELECTOR)
    names = []
    for team in teams:
        href = team.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_sport24_article(uri):
    driver.get(f'{sport24.BASE_URL}{uri}')
    url = driver.find_element(By.CSS_SELECTOR, sport24.ARTICLE_URL_SELECTOR).get_attribute('href').strip()
    driver.get(url)
    content = driver.find_element(By.CSS_SELECTOR, sport24.ARTICLE_CONTENT_SELECTOR)

    return {
        "author": content.find_element(By.CSS_SELECTOR, sport24.AUTHOR_SELECTOR).text,
        "date": content.find_element(By.CSS_SELECTOR, sport24.DATE_SELECTOR).text.split(' ')[0].strip(),
        "time": content.find_element(By.CSS_SELECTOR, sport24.TIME_SELECTOR).text.split(' ')[-1].strip(),
        "img": content.find_element(By.CSS_SELECTOR, sport24.IMAGE_SELECTOR).get_attribute('srcset').split(',')[1].strip().split(' ')[0],
        "thumbnail": content.find_element(By.CSS_SELECTOR, sport24.THUMBNAIL_SELECTOR).get_attribute('srcset').split(',')[0].split(' ')[0],
        "title": content.find_element(By.CSS_SELECTOR, sport24.TITLE_SELECTOR).text.strip(),
        "body": [{tag.tag_name:tag.text} for tag in content.find_elements(By.CSS_SELECTOR, sport24.BODY_SELECTOR)]
    }

# driver.quit()
