from math import floor

tournaments = int(input())
start_points = int(input())

points = 0
win_tour = 0

for _ in range(tournaments):
    tour = input()

    if tour == 'W':
        points += 2000
        win_tour += 1
    elif tour == 'F':
        points += 1200
    elif tour == 'SF':
        points += 720

print(f'Final points: {start_points + points:}')
print(f'Average points: {floor(points / tournaments)}')
print(f'{(win_tour / tournaments) * 100:.2f}%')
