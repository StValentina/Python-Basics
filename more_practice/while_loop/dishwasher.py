DETERGENT = 750

bottles = int(input())

detergent_amount = 0
total_detergent = 0
dishes_counter = 0
dishes_detergent = 0
pots_counter = 0
pots_detergent = 0
counter = 0

while total_detergent <= detergent_amount:
    amount = input()

    if amount == 'End':
        break

    if counter == 2:
        pots_counter += int(amount)
        pots_detergent += int(amount) * 15
        counter = 0
    else:
        dishes_counter += int(amount)
        dishes_detergent += int(amount) * 5
        counter += 1

    detergent_amount = bottles * DETERGENT
    total_detergent = dishes_detergent + pots_detergent

if total_detergent <= detergent_amount:
    print('Detergent was enough!')
    print(f'{dishes_counter} dishes and {pots_counter} pots were washed.')
    print(f'Leftover detergent {detergent_amount - total_detergent} ml.')
else:
    print(f'Not enough detergent, {total_detergent - detergent_amount} ml. more necessary!')



