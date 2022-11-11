"""
The urls and the selectors for all operations in sport24 website
"""

# // WEBSITE
BASE_URL = 'https://www.sport24.gr/'
DATE_FORMAT = '%d.%m.%Y'

# // FOOTBALL
GREEK_FOOTBALL_COMPETITIONS_SELECTOR = '.main-menu__side-panel-container > :nth-child(3) > div > :first-child [itemprop="url"]'
INTERNATIONAL_FOOTBALL_COMPETITIONS_SELECTOR = '.main-menu__side-panel-container > :nth-child(3) > div > :nth-child(2) [itemprop="url"]'
GREEK_FOOTBALL_TEAMS_SELECTOR = '[class*="teams_football_greece"] [itemprop="url"]'
INTERNATIONAL_FOOTBALL_TEAMS_SELECTOR = '[class*="teams_football_international"] [itemprop="url"]'

# // BASKETBALL
GREEK_BASKETBALL_TEAMS_SELECTOR = '[class*="teams_basketball_greece"] [itemprop="url"]'
EUROLEAGUE_TEAMS_SELECTOR = '[class*="teams_basketball_euroleague"] [itemprop="url"]'
NBA_TEAMS_SELECTOR = '[class*="teams_basketball_nba"] [itemprop="url"]'

# // ARTICLE
ARTICLE_URL_SELECTOR = '.teaser__content a'
ARTICLE_CONTENT_SELECTOR = '#article-container'
AUTHOR_SELECTOR = '.article-single__byline span'
DATE_SELECTOR = '.article-single__byline > time'
TIME_SELECTOR = '.article-single__byline > time'
IMAGE_SELECTOR = '.article-single__image--main > img'
TITLE_SELECTOR = '.article-single__title'
BODY_SELECTOR = '.article-single__body > p'
