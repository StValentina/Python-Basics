from math import floor, ceil

days = int(input())
food_for_everybody_kilo = int(input())
dogs_food_of_day_kilo = float(input())
cats_food_of_day_kilo = float(input())
turtles_food_of_day_gram = float(input())

dogs_food = dogs_food_of_day_kilo * days
cats_food = cats_food_of_day_kilo * days
turtles_food = turtles_food_of_day_gram * days / 1000
total_food = dogs_food + cats_food + turtles_food

if total_food <= food_for_everybody_kilo:
    print(f"{floor(food_for_everybody_kilo - total_food)} kilos of food left.")
else:
    print(f"{ceil(total_food - food_for_everybody_kilo)} more kilos of food are needed.")