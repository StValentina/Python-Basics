moves = int(input())

score = 0
number_one, number_two, number_three, number_four, number_five, number_six = 0, 0, 0, 0, 0, 0

for _ in range(1, moves + 1):
    number = int(input())

    if 0 <= number <= 9:
        score += number * 0.20
        number_one += 1
    elif 10 <= number <= 19:
        score += number * 0.30
        number_two += 1
    elif 20 <= number <= 29:
        score += number * 0.40
        number_three += 1
    elif 30 <= number <= 39:
        score += 50
        number_four += 1
    elif 40 <= number <= 50:
        score += 100
        number_five += 1
    elif 50 < number or number < 0:
        score = score / 2
        number_six += 1

print(f'{score:.2f}')
print(f'From 0 to 9: {(number_one / moves) * 100:.2f}%')
print(f'From 10 to 19: {(number_two / moves) * 100:.2f}%')
print(f'From 20 to 29: {(number_three / moves) * 100:.2f}%')
print(f'From 30 to 39: {(number_four / moves) * 100:.2f}%')
print(f'From 40 to 50: {(number_five / moves) * 100:.2f}%')
print(f'Invalid numbers: {(number_six / moves) * 100:.2f}%')

