flour_price = float(input())
flour_kilo = float(input())
sugar_kilo = float(input())
eggs_amount = int(input())
yeast_amount = int(input())

sugar_price = flour_price - flour_price * 0.25
eggs_price = flour_price + flour_price * 0.10
yeast_price = sugar_price - sugar_price * 0.80

total = (
    flour_kilo * flour_price
        +
    sugar_kilo * sugar_price
        +
    eggs_amount * eggs_price
        +
    yeast_amount + yeast_price
    )
    
print(f'{total:.2f}')