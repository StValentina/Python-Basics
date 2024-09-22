games = 0
wins = 0
loses = 0
tournaments = 0

while True:
    tournament_name = input()

    if tournament_name == 'End of tournaments':
        break

    match_amount = int(input())
    games = 0

    for _ in range(match_amount):
        desi_team_points = int(input())
        other_team_points = int(input())
        games += 1

        if desi_team_points > other_team_points:
            wins += 1
            print(f'Game {games} of tournament {tournament_name}: '
                  f'win with {desi_team_points - other_team_points} points.')
        else:
            loses += 1
            print(f'Game {games} of tournament {tournament_name}: '
                  f'lost with {other_team_points - desi_team_points} points.')

        tournaments += 1

print(f'{(wins / tournaments) * 100:.2f}% matches win')
print(f'{(loses / tournaments) * 100:.2f}% matches lost')
