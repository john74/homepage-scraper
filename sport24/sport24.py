from datetime import datetime, date
from fastapi import APIRouter

from . import scraper, variables
router = APIRouter()

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
        article = scraper.get_article(url)
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

@router.get("/api/greek-football-articles")
async def fetch_greek_football_articles():
    """
    Returns the articles from football > Greece > <category>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.GREEK_FOOTBALL_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/international-football-articles")
async def fetch_international_football_articles():
    """
    Returns the articles from football > International > <category>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.INTERNATIONAL_FOOTBALL_COMPETITIONS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/greek-football-teams-articles")
async def fetch_greek_football_teams_articles():
    """
    Returns the articles from football > Greek teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.GREEK_FOOTBALL_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/international-football-teams-articles")
async def fetch_international_football_teams_articles():
    """
    Returns the articles from football > top teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.INTERNATIONAL_FOOTBALL_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/greek-basketball-teams-articles")
async def fetch_greek_basketball_teams_articles():
    """
    Returns the articles from basketball > Greek teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.GREEK_BASKETBALL_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/euroleague-articles")
async def fetch_euroleague_articles():
    """
    Returns the articles from basketball > Euroleague teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.EUROLEAGUE_TEAMS_SELECTOR)
    return await get_articles(category_urls)

@router.get("/api/nba-articles")
async def fetch_nba_articles():
    """
    Returns the articles from basketball > NBA teams > <team>
    navbar menu
    """
    category_urls = scraper.get_category_urls(variables.NBA_TEAMS_SELECTOR)
    return await get_articles(category_urls)
