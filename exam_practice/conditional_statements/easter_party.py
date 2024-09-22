guests_number = int(input())
price_for_one_person = float(input())
budget = float(input())

if guests_number > 20:
    price_for_one_person *= 0.75
elif 15 < guests_number <= 20:
    price_for_one_person *= 0.80
elif 10 <= guests_number <= 15:
    price_for_one_person *= 0.85

price_for_all = price_for_one_person * guests_number
cake_price = budget * 0.10
total_for_party = price_for_all + cake_price

if budget > total_for_party:
    print(f'It is party time! {abs(total_for_party - budget)} leva left.')
else:
    print(f'No party! {abs(budget - total_for_party)} leva needed.')