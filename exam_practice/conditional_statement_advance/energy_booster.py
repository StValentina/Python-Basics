fruit = input()
sets = input()
set_amount = int(input())

set_price = 0
total_price = 0

if fruit == 'Watermelon':
    if sets == 'small':
        set_price = set_amount * (56 * 2)
    elif sets == 'big':
        set_price = set_amount * (28.70 * 5)

elif fruit == 'Mango':
    if sets == 'small':
        set_price = set_amount * (36.66 * 2)
    elif sets == 'big':
        set_price = set_amount * (19.60 * 5)

elif fruit == 'Pineapple':
    if sets == 'small':
        set_price = set_amount * (42.10 * 2)
    elif sets == 'big':
        set_price = set_amount * (24.80 * 5)

elif fruit == 'Raspberry':
    if sets == 'small':
        set_price = set_amount * (20 * 2)
    elif sets == 'big':
        set_price = set_amount * (15.20 * 5)

if 400 <= set_price <= 1000:
    total_price = set_price * 0.85
elif 1000 < set_price:
    total_price = set_price * 0.50
else:
    total_price = set_price

print(f'{total_price:.2f} lv.')
