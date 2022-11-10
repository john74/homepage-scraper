import os, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from . import variables

service = Service(f'{os.getcwd()}/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

def get_category_names(selector):
    driver.get(variables.BASE_URL)
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    names = []
    for element in elements:
        href = element.get_attribute('href')
        name = href.split('/')[-1]
        names.append(name.strip())
    return names

def get_article(uri):
    driver.get(f'{variables.BASE_URL}{uri}')
    anchor_element = driver.find_element(By.CSS_SELECTOR, variables.ARTICLE_URL_SELECTOR)
    url = anchor_element.get_attribute('href').strip()
    driver.get(url)

    try:
        content = driver.find_element(By.CSS_SELECTOR, variables.ARTICLE_CONTENT_SELECTOR)
    except Exception:
        return

    author = content.find_element(By.CSS_SELECTOR, variables.AUTHOR_SELECTOR).text
    datetime = content.find_element(By.CSS_SELECTOR, variables.DATE_SELECTOR).text.split(' ')
    date = datetime[0]
    time = datetime[-1]
    image_element = content.find_element(By.CSS_SELECTOR, variables.IMAGE_SELECTOR)
    images = re.findall('(https?.+\\.+\\w+)', image_element.get_attribute('srcset'))
    small_image = images[0]
    medium_image = images[1]
    large_image = images[3]
    title = content.find_element(By.CSS_SELECTOR, variables.TITLE_SELECTOR).text

    body = []
    article_body = content.find_elements(By.CSS_SELECTOR, variables.BODY_SELECTOR)
    for tag in article_body:
        text = tag.text
        if len(text):
            body.append(text.strip())

    return {
        "author": author.strip(),
        "date": date.strip(),
        "time": time.strip(),
        "small_image": small_image.strip(),
        "medium_image": medium_image.strip(),
        "large_image": large_image.strip(),
        "title": title.strip(),
        "body": body
    }

# driver.quit()
