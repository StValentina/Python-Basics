from math import floor, ceil

X_vineyard = int(input())
Y_grape = float(input())
Z_wine = int(input())
workers = int(input())

sum_of_grape = X_vineyard * Y_grape
wine = 0.40 * sum_of_grape / 2.5

if wine < Z_wine:
    print(f"It will be a tough winter! More {floor(Z_wine - wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(wine - Z_wine)} liters left -> {ceil((wine - Z_wine) / workers)} liters per person.")
