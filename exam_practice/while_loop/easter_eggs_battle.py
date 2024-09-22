player_one_point = int(input())
player_two_point = int(input())

while player_one_point > 0 and player_two_point > 0:
    command = input()

    if command == 'End':
        print(f'Player one has {player_one_point} eggs left.')
        print(f'Player two has {player_two_point} eggs left.')
        break

    if command == 'one':
        player_two_point -= 1
    elif command == 'two':
        player_one_point -= 1

    if player_one_point == 0:
        print(f'Player one is out of eggs. Player two has {player_two_point} eggs left.')
    elif player_two_point == 0:
        print(f'Player two is out of eggs. Player one has {player_one_point} eggs left.')
