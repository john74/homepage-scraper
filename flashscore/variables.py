"""
The urls and the selectors for all operations in sport24 website
"""
FOOTBALL_LEAGUES = {
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
    'url': 'https://www.flashscore.com',
    'standings': 'standings',
    'date_format': '%d.%m.%Y'
}

TEAM = {
    'name': '.tableCellParticipant__name',
    'status': '.tableCellRank',
    'matches_played': ':nth-child(3)',
    'wins': ':nth-child(4)',
    'draws': ':nth-child(5)',
    'losses': ':nth-child(6)',
    'points': '.table__cell--points',
    'next_match_data': '.table__cell--form > :first-child',
    'last_five_results': '.table__cell--form > :not(:first-child)'
}
