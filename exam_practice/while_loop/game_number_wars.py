player_one_name = input()
player_two_name = input()

player_one_points = 0
player_two_points = 0

while True:
    command1 = input()

    if command1 == 'End of game':
        print(f"{player_one_name} has {player_one_points} points")
        print(f"{player_two_name} has {player_two_points} points")
        break
    command2 = int(input())

    points_one = int(command1)
    points_two = int(command2)

    if points_one > points_two:
        player_one_points += points_one - points_two
    elif points_two > points_one:
        player_two_points += points_two - points_one
    elif points_one == points_two:
        print("Number wars!")
        points_one_last = int(input())
        points_two_last = int(input())
        if points_one_last > points_two_last:
            print(f"{player_one_name} is winner with {player_one_points} points")
            break
        else:
            print(f"{player_two_name} is winner with {player_two_points} points")
            break

