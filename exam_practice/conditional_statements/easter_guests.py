from math import ceil

BREAD_PRICE = 4
EGGS_PRICE = 0.45

guests_number = int(input())
budget = int(input())

buy_a_bread = ceil(guests_number / 3)
sum_of_bread = buy_a_bread * BREAD_PRICE
buy_a_eggs = guests_number * 2
sum_of_eggs = buy_a_eggs * EGGS_PRICE
total = sum_of_eggs + sum_of_bread

if budget > total:
    print(f'Lyubo bought {buy_a_bread} Easter bread and {buy_a_eggs} eggs.')
    print(f'He has {budget - total:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {total - budget:.2f} lv. more.')