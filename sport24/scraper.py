import re
from datetime import datetime, date
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from driver import driver
from .variables import WEBSITE, ARTICLE


def get_category_urls(anchor_elements):
    """
    Accepts the css selector of all a tags of the category.
    Returns a set containing the urls from all a tags.
    """
    driver.get(WEBSITE['url'])
    anchor_elements = driver.find_elements(By.CSS_SELECTOR, anchor_elements)
    urls = set()
    for anchor in anchor_elements:
        url = anchor.get_attribute('href')
        urls.add(url.strip())
    return urls


def get_category_name_url_pairs(category_urls):
    """
    Returns the names of the categories and the category urls
    as key value pairs.
    key: the part after the last / of the category url.
    value: the category url.
    """
    pairs = {}
    for url in category_urls:
        category = url.split('/')[-1]
        pairs[category] = url
    return pairs


def get_recent_articles(category_name_url_pairs):
    """
    Returns the name of the category and the url of the
    first article of each category as key value pairs,
    if the article is less that 4 days old.
    KEY: the category name.
    VALUE: the url of the first article.
    """
    recent_articles = {}
    for name, url in category_name_url_pairs.items():
        driver.get(url)
        post_date_info_list = driver.find_element(
            By.CSS_SELECTOR, ARTICLE['post_date']
        ).text.lower().split(' ')
        time_unit = post_date_info_list[1]
        time_value = int(post_date_info_list[0])
        article_is_recent = time_unit != ARTICLE['time_unit'] or \
                            time_value < ARTICLE['time_value']
        if article_is_recent:
            anchor_element = driver.find_element(By.CSS_SELECTOR, ARTICLE['url'])
            article_url = anchor_element.get_attribute('href')
            recent_articles[name] = article_url.strip()
    return recent_articles


def get_unique_pairs(recent_articles):
    """
    Rejects the keys that have the same value with other keys
    in the dictionary, and returns the unique pairs.
    """
    pairs = {}
    urls = []
    for category, url in recent_articles.items():
        if url in urls:
            continue
        urls.append(url)
        pairs[category] = url
    return pairs
