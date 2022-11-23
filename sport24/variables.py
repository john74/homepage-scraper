"""
The urls and the selectors for all operations in sport24 website
"""
CATEGORY_SELECTORS = {
    # // FOOTBALL
    'greek_football': 'nav > div > :nth-child(3) > div > :nth-child(1) a',
    'international_football': 'nav > div > :nth-child(3) > div > :nth-child(2) a',
    'greek_football_teams': '[class*="teams_football_greece"] a',
    'international_football_teams': '[class*="teams_football_international"] a',

    # // BASKETBALL
    'greek_basketball_teams': '[class*="teams_basketball_greece"] a',
    'euroleague_teams': '[class*="teams_basketball_euroleague"] a',
    'nba_teams': '[class*="teams_basketball_nba"] a'
}

WEBSITE = {
    'url': 'https://www.sport24.gr/',
    'name': 'sport24.gr',
    'date_format': '%d.%m.%Y'
}

ARTICLE = {
    'url': '.article__title > a',
    'title': '.article-single__title',
    'content': '#article-container',
    'author': '.article-single__byline span',
    'datetime': '.article-single__byline > time',
    'image': 'figure > [srcset]',
    'images': r'(http.+\w+),?',
    'body': '.article-single__body > p'
}

REJECTED_TITLE_SUBSTRINGS = [
    ": Η βαθμολογία ",
    "Αθλητικές μεταδόσεις:"
]

REJECTED_URL_SUBSTRINGS = [
    'longreads'
]
