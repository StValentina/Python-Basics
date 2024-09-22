from math import floor, ceil

price_for_one_tennis_racket = float(input())
amount_of_tennis_racket = int(input())
amount_of_shoes = int(input())

sum_for_tennis_rackets = amount_of_tennis_racket * price_for_one_tennis_racket
price_for_one_shoe = price_for_one_tennis_racket / 6
sum_for_shoes = amount_of_shoes * price_for_one_shoe
other_equipment = (sum_for_tennis_rackets + sum_for_shoes) * 0.20
total = sum_for_tennis_rackets + sum_for_shoes + other_equipment

price_for_djockovich = total / 8
price_for_sponsors = total * 7 / 8

print(f'Price to be paid by Djokovic')
print(floor(price_for_djockovich))
print(f'Price to be paid by sponsors')
print(ceil(price_for_sponsors))
