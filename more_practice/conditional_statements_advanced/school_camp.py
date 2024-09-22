season = input()
group = input()
students = int(input())
nights = int(input())

sport = None
price = 0

if group == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
        price = students * 9.60 * nights
    elif season == 'Spring':
        sport = 'Athletics'
        price = students * 7.20 * nights
    elif season == 'Summer':
        sport = 'Volleyball'
        price = students * 15 * nights
elif group == 'boys':
    if season == 'Winter':
        sport = 'Judo'
        price = students * 9.60 * nights
    elif season == 'Spring':
        sport = 'Tennis'
        price = students * 7.20 * nights
    elif season == 'Summer':
        sport = 'Football'
        price = students * 15 * nights
elif group == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
        price = students * 10 * nights
    elif season == 'Spring':
        sport = 'Cycling'
        price = students * 9.50 * nights
    elif season == 'Summer':
        sport = 'Swimming'
        price = students * 20 * nights

if students >= 50:
    price *= 0.50
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

print(f'{sport} {price:.2f} lv.')