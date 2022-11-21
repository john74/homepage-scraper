import os, re
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from .variables import WEBSITE, ARTICLE


service = Service(f'{os.getcwd()}/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(service=service, options=option)

def get_category_urls(css_selector):
    """
    Returns a list of urls for each category in sport24.gr navbar
    as specified by the css_selector parameter.
    """
    driver.get(WEBSITE['url'])
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
    anchor_element = driver.find_element(By.CSS_SELECTOR, ARTICLE['url'])
    article_url = anchor_element.get_attribute('href').strip()
    driver.get(article_url)

    try:
        content = driver.find_element(By.CSS_SELECTOR, ARTICLE['content'])
    except Exception:
        return

    author = content.find_element(By.CSS_SELECTOR, ARTICLE['author']).text
    date_time = content.find_element(By.CSS_SELECTOR, ARTICLE['datetime']).text.split(' ')
    post_date = date_time[0]
    post_time = date_time[-1]
    image_element = content.find_element(By.CSS_SELECTOR, ARTICLE['image'])
    images_list = re.findall(ARTICLE['image_list'], image_element.get_attribute('srcset'))
    small_image = images_list[0].split(' ')[0]
    medium_image = images_list[1].split(' ')[0]
    large_image = images_list[3].split(' ')[0]
    title = content.find_element(By.CSS_SELECTOR, ARTICLE['title']).text

    body = ''
    article_body = content.find_elements(By.CSS_SELECTOR, ARTICLE['body'])
    for tag in article_body:
        text = tag.text
        text_has_more_than_ten_words = len(text.split(' ')) > 10
        if text_has_more_than_ten_words:
            body += text.strip() + '\n'

    if not body:
        return

    return {
        "website": "sport24.gr",
        "category": category_url.split('/')[-1],
        "url": article_url,
        "author": author.strip(),
        "date": post_date.strip(),
        "time": post_time.strip(),
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

    # articles = {}
    articles = []
    titles = []
    rejected_titles_substrings = [
        ": Η βαθμολογία ", "Αθλητικές μεταδόσεις:"
    ]

    today = datetime.strptime(date.today().strftime(WEBSITE['date_format']), WEBSITE['date_format'])
    for url in category_urls:
        article = get_article(url)
        if article is None:
            continue
        title = article['title']
        is_unique = title not in titles
        days_since_post = (today - datetime.strptime(article['date'], WEBSITE['date_format'])).days
        is_recent = days_since_post <= 7

        title_is_accepted = True
        for substring in rejected_titles_substrings:
            if substring.lower() in title.lower():
                title_is_accepted = False
                break

        if is_unique and is_recent and title_is_accepted:
            titles.append(title)
            articles.append(article)
            # article_category = url.split('/')[-1]
            # articles[article_category] = article

    return articles
