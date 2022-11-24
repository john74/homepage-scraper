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


def get_category_name_article_url_pairs(category_name_url_pairs):
    """
    Returns the name of the category and the url of the
    first article of each category as key value pairs.
    key: the category name.
    value: the url of the first article.
    """
    article_urls = {}
    for name, url in category_name_url_pairs.items():
        driver.get(url)
        anchor_element = driver.find_element(By.CSS_SELECTOR, ARTICLE['url'])
        article_url = anchor_element.get_attribute('href')
        article_urls[name] = article_url.strip()
    return article_urls
