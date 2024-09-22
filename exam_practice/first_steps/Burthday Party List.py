rent_for_hall = float(input())

cake_price = rent_for_hall * 0.20
drinks_price = cake_price - cake_price * 0.45
animator = rent_for_hall / 3

total = rent_for_hall + cake_price + drinks_price + animator

print(total)