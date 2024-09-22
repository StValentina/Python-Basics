inherited_money = float(input())
years_living = int(input())

ages = 18
received_money = 0

for years in range(1800, years_living + 1):

    if years % 2 == 0:
        received_money += 12000
        ages += 1
    else:
        received_money += 12000 + (50 * ages)
        ages += 1

money_for_living = inherited_money - received_money

if inherited_money >= received_money:
    print(f'Yes! He will live a carefree life and will have {money_for_living:.2f} dollars left.')
else:
    print(f'He will need {abs(inherited_money - received_money):.2f} dollars to survive.')
