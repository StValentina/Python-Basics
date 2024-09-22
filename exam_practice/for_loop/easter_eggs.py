coloured_eggs_amount = int(input())

red_eggs, orange_eggs, blue_eggs, green_eggs = 0, 0, 0, 0
max_eggs = 0
colour_max = None

for _ in range(coloured_eggs_amount):
    colour = input()

    if colour == 'red':
        red_eggs += 1
    elif colour == 'orange':
        orange_eggs += 1
    elif colour == 'blue':
        blue_eggs += 1
    elif colour == 'green':
        green_eggs += 1

    if red_eggs > max_eggs:
        max_eggs = red_eggs
        colour_max = 'red'
    elif orange_eggs > max_eggs:
        max_eggs = orange_eggs
        colour_max = 'orange'
    elif blue_eggs > max_eggs:
        max_eggs = blue_eggs
        colour_max = 'blue'
    elif green_eggs > max_eggs:
        max_eggs = green_eggs
        colour_max = 'green'

print(f'Red eggs: {red_eggs}\nOrange eggs: {orange_eggs}\nBlue eggs: {blue_eggs}\nGreen eggs: {green_eggs}')
print(f'Max eggs: {max_eggs} -> {colour_max}')