import os, re
from datetime import datetime, date
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

def get_category_urls(css_selector):
    """
    Returns a list of urls for each category in sport24.gr navbar
    as specified by the css_selector parameter.
    """
    driver.get(variables.BASE_URL)
    elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
    urls = []
    for element in elements:
        href = element.get_attribute('href')
        urls.append(href)
    return urls

def get_article(category_url):
    """
    Returns the content of the first article for the category
    specified by the category_url parameter.
    """
    driver.get(category_url)
    anchor_element = driver.find_element(By.CSS_SELECTOR, variables.ARTICLE_URL_SELECTOR)
    article_url = anchor_element.get_attribute('href').strip()
    driver.get(article_url)

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

async def get_articles(category_urls):
    """
    Returns a list of articles. An article is accepted
    if it is unique, not older than a week and the title
    doesn't contain a substring from rejected_titles_substrings
    """
    articles = []
    titles = []
    rejected_titles_substrings = [
        ": Η βαθμολογία ", "Αθλητικές μεταδόσεις:"
    ]

    today = datetime.strptime(date.today().strftime(variables.DATE_FORMAT), variables.DATE_FORMAT)
    for url in category_urls:
        article = get_article(url)
        if article is None:
            continue
        title = article['title']
        is_unique = title not in titles
        days_since_post = (today - datetime.strptime(article['date'], variables.DATE_FORMAT)).days
        is_recent = days_since_post <= 7

        title_is_accepted = True
        for substring in rejected_titles_substrings:
            if substring.lower() in title.lower():
                title_is_accepted = False
                break

        if is_unique and is_recent and title_is_accepted:
            titles.append(title)
            articles.append(article)
    return articles
# driver.quit()
