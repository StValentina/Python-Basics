season = input()
kilometers_month = float(input())

salary = 0

if kilometers_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        salary = (kilometers_month * 0.75) * 4 * 0.90
    elif season == 'Summer':
        salary = (kilometers_month * 0.90) * 4 * 0.90
    elif season == 'Winter':
        salary = (kilometers_month * 1.05) * 4 * 0.90
elif 5000 < kilometers_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        salary = (kilometers_month * 0.95) * 4 * 0.90
    elif season == 'Summer':
        salary = (kilometers_month * 1.10) * 4 * 0.90
    elif season == 'Winter':
        salary = (kilometers_month * 1.25) * 4 * 0.90
elif 10000 < kilometers_month <= 20000:
    salary = (kilometers_month * 1.45) * 4 * 0.90

print(f'{salary:.2f}')
