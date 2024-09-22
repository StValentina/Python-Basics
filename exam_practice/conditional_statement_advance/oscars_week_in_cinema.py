movie = input()
hall = input()
tickets = int(input())

income = 0

if movie == 'A Star Is Born':
    if hall == 'normal':
        income = tickets * 7.50
    elif hall == 'luxury':
        income = tickets * 10.50
    elif hall == 'ultra luxury':
        income = tickets * 13.50

elif movie == 'Bohemian Rhapsody':
    if hall == 'normal':
        income = tickets * 7.35
    elif hall == 'luxury':
        income = tickets * 9.45
    elif hall == 'ultra luxury':
        income = tickets * 12.75

elif movie == 'Green Book':
    if hall == 'normal':
        income = tickets * 8.15
    elif hall == 'luxury':
        income = tickets * 10.25
    elif hall == 'ultra luxury':
        income = tickets * 13.25

elif movie == 'The Favourite':
    if hall == 'normal':
        income = tickets * 8.75
    elif hall == 'luxury':
        income = tickets * 11.55
    elif hall == 'ultra luxury':
        income = tickets * 13.95

print(f'{movie} -> {income:.2f} lv.')