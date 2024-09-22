juniors_amount = int(input())
seniors_amount = int(input())
trace = input()

total = 0

if trace == 'trail':
    juniors = juniors_amount * 5.50
    seniors = seniors_amount * 7
    total = juniors + seniors

elif trace == 'cross-country':
    juniors = juniors_amount * 8
    seniors = seniors_amount * 9.50
    total = juniors + seniors
    if (juniors_amount + seniors_amount) >= 50:
        total *= 0.75

elif trace == 'downhill':
    juniors = juniors_amount * 12.25
    seniors = seniors_amount * 13.75
    total = juniors + seniors

elif trace == 'road':
    juniors = juniors_amount * 20
    seniors = seniors_amount * 21.50
    total = juniors + seniors

expenses = total * 0.05

print(f'{total - expenses:.2f}')
