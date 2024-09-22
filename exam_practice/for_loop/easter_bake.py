from math import ceil
easter_bread_amount = int(input())

sugar_amount = 0
flour_amount = 0
max_sugar = 0
max_flour = 0

for _ in range(easter_bread_amount):
    sugar = int(input())
    flour = int(input())

    sugar_amount += sugar
    flour_amount += flour

    if sugar >= max_sugar:
        max_sugar = sugar

    if flour >= max_flour:
        max_flour = flour

print(f'Sugar: {ceil(sugar_amount / 950)}')
print(f'Flour: {ceil(flour_amount / 750)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')