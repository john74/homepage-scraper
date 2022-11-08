import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


service = Service(f'{os.getcwd()}/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

def get_sport24_greek_competitions():
    driver.get('https://www.sport24.gr')
    competitions = driver.find_elements(By.CSS_SELECTOR, '.main-menu__side-panel-container > :nth-child(3) > .main-menu__dropdown main-menu__dropdown--mega-menu [itemprop="url"')

def get_sport24_greek_team_names():
    driver.get('https://www.sport24.gr')
    teams = driver.find_elements(By.CSS_SELECTOR, '.main-menu__group--teams_football_greece [itemprop="url"')
    names = []
    for team in teams:
        href = team.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_sport24_international_team_names():
    driver.get('https://www.sport24.gr')
    teams = driver.find_elements(By.CSS_SELECTOR, '.main-menu__group--teams_football_international [itemprop="url"')
    names = []
    for team in teams:
        href = team.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_sport24_article(uri):
    driver.get(f'https://www.sport24.gr/{uri}')
    url = driver.find_element(By.CSS_SELECTOR, '.teaser__content > :first-child .article__image > a').get_attribute('href').strip()
    driver.get(url)
    content = driver.find_element(By.CSS_SELECTOR, '.article-single')

    return {
        "author": content.find_element(By.CSS_SELECTOR, '.article-single__byline span').text,
        "date": content.find_element(By.CSS_SELECTOR, '.article-single__byline > time').text.split(' ')[0].strip(),
        "time": content.find_element(By.CSS_SELECTOR, '.article-single__byline > time').text.split(' ')[-1].strip(),
        "img": content.find_element(By.CSS_SELECTOR, '.article-single__image--main > img').get_attribute('srcset').split(',')[1].strip().split(' ')[0],
        "thumbnail": content.find_element(By.CSS_SELECTOR, '.article-single__image--main > img').get_attribute('srcset').split(',')[0].split(' ')[0],
        "title": content.find_element(By.CSS_SELECTOR, '.article-single__title').text.strip(),
        "body": [{tag.tag_name:tag.text} for tag in content.find_elements(By.CSS_SELECTOR, '.article-single__body > h2,p')]
    }

# driver.quit()
