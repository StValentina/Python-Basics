START_PRICE_TAXI = 0.70

kilometers = int(input())
day_or_night = str(input())

price = 0.00
taxi_price = 0.00

if day_or_night == 'day':
    taxi_price = 0.79
else:
    taxi_price = 0.90

if kilometers < 20:
    price = START_PRICE_TAXI + (kilometers * taxi_price)
elif kilometers < 100:
    price = kilometers * 0.09
else:
    price = kilometers * 0.06

print(f'{price:.2f}')
