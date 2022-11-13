"""
The urls and the selectors for all operations in sport24 website
"""
FOOTBALL_LEAGUES = {
    # // FOOTBALL
    'austria': ['bundesliga'],
    'belgium': ['jupiler-pro-league'],
    'czech-republic': ['1-liga'],
    'denmark': ['superliga'],
    'england': ['premier-league', 'championship', 'league-one', 'league-two'],
    'france': ['ligue-1', 'ligue-2'],
    'germany': ['bundesliga', '2-bundesliga', '3-liga'],
    'greece': ['super-league', 'super-league-2', 'football-league'],
    'italy': ['serie-a', 'serie-b'],
    'netherlands': ['eredivisie', 'eerste-divisie'],
    'norway': ['eliteserien'],
    'poland': ['ekstraklasa'],
    'portugal': ['liga-portugal', 'liga-portugal-2'],
    'romania': ['liga-1'],
    'russia': ['premier-league'],
    'scotland': ['premiership'],
    'serbia': ['super-liga'],
    'slovakia': ['fortuna-liga'],
    'slovenia': ['prva-liga'],
    'spain': ['laliga', 'laliga2'],
    'sweden': ['allsvenskan'],
    'switzerland': ['super-league'],
    'turkey': ['super-lig'],
    'ukraine': ['premier-league'],

    # // BASKETBALL
    'greek_basketball_teams': '[class*="teams_basketball_greece"] a',
    'euroleague_teams': '[class*="teams_basketball_euroleague"] a',
    'nba_teams': '[class*="teams_basketball_nba"] a'
}

WEBSITE = {
    'url': 'https://www.flashscore.com/',
    'date_format': '%d.%m.%Y'
}

ARTICLE = {
    'url': '.article__title a',
    'title': '.article-single__title',
    'content': '#article-container',
    'author': '.article-single__byline span',
    'datetime': '.article-single__byline > time',
    'image': 'figure > img',
    'body': '.article-single__body > p'
}
