"""
The urls and the selectors for all operations in sport24 website
"""
BASE_URL = 'https://www.sport24.gr/'
GREEK_COMPETITIONS_SELECTOR = '.main-menu__side-panel-container > :nth-child(3) > div > :first-child [itemprop="url"]'
INTERNATIONAL_COMPETITIONS_SELECTOR = '.main-menu__side-panel-container > :nth-child(3) > div > :nth-child(2) [itemprop="url"]'
GREEK_TEAMS_SELECTOR = '.main-menu__group--teams_football_greece [itemprop="url"]'
INTERNATIONAL_TEAMS_SELECTOR = '.main-menu__group--teams_football_international [itemprop="url"]'
ARTICLE_URL_SELECTOR = '.teaser__content > :first-child .article__image > a'
ARTICLE_CONTENT_SELECTOR = '#article-container'
AUTHOR_SELECTOR = '.article-single__byline span'
DATE_SELECTOR = '.article-single__byline > time'
TIME_SELECTOR = '.article-single__byline > time'
IMAGE_SELECTOR = '.article-single__image--main > img'
THUMBNAIL_SELECTOR = '.article-single__image--main > img'
TITLE_SELECTOR = '.article-single__title'
BODY_SELECTOR = '.article-single__body > p'
DATE_FORMAT = '%d.%m.%Y'
