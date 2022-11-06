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

teams = ['panathinaikos', 'olympiacos', 'aek', 'paok', 'aris']
def get_sport24_team_articles(teams):
  articles = []
  titles = []
  for team in teams:
    url = f'https://www.sport24.gr/football/{team}'
    driver.get(url)
    preview_content = driver.find_element(By.CSS_SELECTOR, '.teaser__content > :first-child')
    link = preview_content.find_element(By.CSS_SELECTOR, '.article__image > a').get_attribute('href').strip()
    driver.get(link)
    content = driver.find_element(By.CSS_SELECTOR, '.article-single')
    article_title = content.find_element(By.CSS_SELECTOR, '.article-single__title').text.strip()
    if article_title in titles: continue
    titles.append(article_title)
    article_body = [{tag.tag_name:tag.text} for tag in content.find_elements(By.CSS_SELECTOR, '.article-single__body > h2,p')]

    articles.append({
      "website": "sport24",
      "team": team,
      "author": content.find_element(By.CSS_SELECTOR, '.article-single__byline__author').text.strip(),
      "post_date": content.find_element(By.CSS_SELECTOR, '.article-single__byline > time').text.split(' ')[0].strip(),
      "post_time": content.find_element(By.CSS_SELECTOR, '.article-single__byline > time').text.split(' ')[-1].strip(),
      "article_img_link": content.find_element(By.CSS_SELECTOR, '.article-single__image--main > img').get_attribute('srcset').split(',')[1].strip().split(' ')[0],
      "article_small_img_link": content.find_element(By.CSS_SELECTOR, '.article-single__image--main > img').get_attribute('srcset').split(',')[0].split(' ')[0],
      "article_title": article_title,
      "article_body": article_body
    })

  driver.quit()
  return articles

# get_sport24_team_articles(teams)
