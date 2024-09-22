egg_size = input()
egg_colour = input()
egg_amount = int(input())

egg_price = 0
expenses = 0

if egg_size == 'Large':
    if egg_colour == 'Red':
        egg_price = egg_amount * 16
    elif egg_colour == 'Green':
        egg_price = egg_amount * 12
    elif egg_colour == 'Yellow':
        egg_price = egg_amount * 9

elif egg_size == 'Medium':
    if egg_colour == 'Red':
        egg_price = egg_amount * 13
    elif egg_colour == 'Green':
        egg_price = egg_amount * 9
    elif egg_colour == 'Yellow':
        egg_price = egg_amount * 7

elif egg_size == 'Small':
    if egg_colour == 'Red':
        egg_price = egg_amount * 9
    elif egg_colour == 'Green':
        egg_price = egg_amount * 8
    elif egg_colour == 'Yellow':
        egg_price = egg_amount * 5

expenses = egg_price * 0.35

print(f'{egg_price - expenses:.2f} leva.')