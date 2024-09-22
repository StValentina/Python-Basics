VIP = 499.99
NORMAL = 249.99

budget = float(input())
category = input()
people = int(input())

price = 0

if 50 <= people:
    budget *= 0.75
elif 25 <= people <= 49:
    budget *= 0.60
elif 10 <= people <= 24:
    budget *= 0.50
elif 5 <= people <= 9:
    budget *= 0.40
else:
    budget *= 0.25

if category == 'Normal':
    price = people * NORMAL
elif category == 'VIP':
    price = people * VIP

if budget > price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')
