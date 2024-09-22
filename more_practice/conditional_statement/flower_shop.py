from math import floor, ceil

MAGNOLIAS = 3.25
HYACINTHS = 4
ROSES = 3.50
CACTI = 8
TAX = 0.05

magnolias_amount = int(input())
hyacinths_amount = int(input())
roses_amount = int(input())
cacti_amount = int(input())
gift_price = float(input())

sum_for_flowers = (
    magnolias_amount * MAGNOLIAS
    +
    hyacinths_amount * HYACINTHS
    +
    cacti_amount * CACTI
    +
    roses_amount * ROSES
)

taxes = sum_for_flowers * TAX
sum_after_taxes = sum_for_flowers - taxes

if sum_after_taxes >= gift_price:
    print(f"She is left with {floor(sum_after_taxes - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - sum_after_taxes)} leva.")