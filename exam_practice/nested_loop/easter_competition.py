participants = int(input())

best_baker_name = ''
best_baker_points = 0

for _ in range(participants):
    baker_name = input()
    points = 0
    command = input()

    while command != 'Stop':
        points += int(command)
        command = input()

    print(f'{baker_name} has {points} points.')

    if points > best_baker_points:
        best_baker_name = baker_name
        best_baker_points = points
        print(f'{best_baker_name} is the new number 1!')

print(f'{best_baker_name} won competition with {best_baker_points} points!')

