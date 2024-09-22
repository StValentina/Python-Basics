visitor_amount = int(input())

back, chest, legs, abs_work, protein_shake, protein_bar = 0, 0, 0, 0, 0, 0

for _ in range(visitor_amount):
    visitor_act = input()

    if visitor_act == 'Back':
        back += 1
    elif visitor_act == 'Chest':
        chest += 1
    elif visitor_act == 'Legs':
        legs += 1
    elif visitor_act == 'Abs':
        abs_work += 1
    elif visitor_act == 'Protein shake':
        protein_shake += 1
    elif visitor_act == 'Protein bar':
        protein_bar += 1

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs_work} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{(back + chest + legs + abs_work) / visitor_amount * 100:.2f}% - work out')
print(f'{(protein_shake + protein_bar) / visitor_amount * 100:.2f}% - protein')
