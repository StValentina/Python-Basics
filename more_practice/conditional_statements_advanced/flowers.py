chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
price = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = chrysanthemums * 2.00
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15

price = chrysanthemums_price + roses_price + tulips_price

if day == 'Y':
    price *= 1.15

if season == 'Spring':
    if tulips > 7:
        price *= 0.95
elif season == 'Winter':
    if roses >= 10:
        price *= 0.90

if (chrysanthemums + roses + tulips) > 20:
    price *= 0.80

bouqiet_price = price + 2

print(f'{bouqiet_price:.2f}')
