START_POINTS = 301

player_name = input()

win_points = 0
current_point = 0
successful_points = 0
unsuccessful_points = 0

while START_POINTS > 0:
    field = input()

    if field == 'Retire':
        print(f'{player_name} retired after {unsuccessful_points} unsuccessful shots.')
        break

    points = int(input())

    if field == 'Single':
        win_points = points
    elif field == 'Double':
        win_points = points * 2
    elif field == 'Triple':
        win_points = points * 3

    if win_points > START_POINTS:
        unsuccessful_points += 1
        continue

    START_POINTS -= win_points
    successful_points += 1

else:
    print(f'{player_name} won the leg with {successful_points} shots.')
