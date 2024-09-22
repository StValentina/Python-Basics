MUSSELS = 7.50

mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kilo_amount = float(input())
fish_kilo_amount = float(input())
mussels_kilo_amount = int(input())

bonito_price = mackerel_price + (mackerel_price * 0.60)
sum_of_bonito = bonito_kilo_amount * bonito_price
fish_price = sprinkle_price + (sprinkle_price * 0.80)
sum_of_fish = fish_kilo_amount * fish_price
mussels_price = mussels_kilo_amount * MUSSELS

total_sum_for_shopping = sum_of_bonito + sum_of_fish + mussels_price

print('%.2f' % total_sum_for_shopping) # нов синтаксис print(f'{total_sum_for_shopping:.2f}')
