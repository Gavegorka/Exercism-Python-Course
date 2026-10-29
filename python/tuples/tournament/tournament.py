result_scores = {
    'win': 3,
    'draw': 1,
    'loss': 0
}

def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    need_len = len(table[0][:table[0].index('|')])
    result_for_teams = {
        'Devastating Donkeys':{'MP':0, 'W':0, 'D':0, 'L':0, 'P':0},
        'Allegoric Alaskans':{'MP':0, 'W':0, 'D':0, 'L':0, 'P':0},
        'Blithering Badgers':{'MP':0, 'W':0, 'D':0, 'L':0, 'P':0},
        'Courageous Californians':{'MP':0, 'W':0, 'D':0, 'L':0, 'P':0}
    }

    for row in rows:
        row = row.split(';')

        team1 = row[0]
        team2 = row[1]
        match_result = row[2]

        result_for_teams[team1]['MP'] += 1
        result_for_teams[team2]['MP'] += 1

        if match_result == 'win':
            result_for_teams[team1]['W'] += 1
            result_for_teams[team2]['L'] += 1
        if match_result == 'loss':
            result_for_teams[team1]['L'] += 1
            result_for_teams[team2]['W'] += 1
        if match_result == 'draw':
            result_for_teams[team1]['D'] += 1
            result_for_teams[team2]['D'] += 1

    for team in result_for_teams:
        result_for_teams[team]['P'] += result_for_teams[team]['W'] * 3 + result_for_teams[team]['D']

    result_for_teams = sorted(result_for_teams.items(), key=lambda item: (-item[1]['P'], item[0],))

    for team in result_for_teams:
        points_str = '| ' + ' | '.join(f'{v:>2}' for k, v in team[1].items())
        team_name_str = team[0]
        result_str = f'{team_name_str:<{need_len}}{points_str}'

        if team[1]['MP'] > 0:
            table.append(result_str)
    return table