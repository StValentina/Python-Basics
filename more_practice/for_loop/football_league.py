stadium_capacity = int(input())
fans_amount = int(input())

fans_in_a, fans_in_b, fans_in_v, fans_in_g = 0, 0, 0, 0

for _ in range(fans_amount):
    sector = input()

    if sector == 'A':
        fans_in_a += 1
    elif sector == 'B':
        fans_in_b += 1
    elif sector == 'V':
        fans_in_v += 1
    elif sector == 'G':
        fans_in_g += 1

print(f'{(fans_in_a / fans_amount) * 100:.2f}%')
print(f'{(fans_in_b / fans_amount) * 100:.2f}%')
print(f'{(fans_in_v / fans_amount) * 100:.2f}%')
print(f'{(fans_in_g / fans_amount) * 100:.2f}%')
print(f'{(fans_in_a + fans_in_b + fans_in_v + fans_in_g) / stadium_capacity * 100:.2f}%')
