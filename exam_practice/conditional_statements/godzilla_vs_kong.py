budget = float(input())
person_amount = int(input())
clothes_price_for_person = float(input())

decor = budget * 0.10
clothes_price = person_amount * clothes_price_for_person
if person_amount > 150:
    clothes_price -= clothes_price * 0.10

total_price_for_movie = decor + clothes_price

if total_price_for_movie > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price_for_movie - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price_for_movie:.2f} leva left.")
