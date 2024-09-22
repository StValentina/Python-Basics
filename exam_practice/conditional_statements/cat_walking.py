minutes_of_day = int(input())
number_of_walks = int(input())
calories_per_day = int(input())

total_minutes = number_of_walks * minutes_of_day
total_calories = total_minutes * 5
balanced_calories = total_calories * 0.50

if total_calories >= balanced_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories}.')