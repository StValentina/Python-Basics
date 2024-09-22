months = int(input())

electricity_price = 0
water = 0
internet = 0
other = 0

for _ in range(months):
    electricity = float(input())
    electricity_price += electricity
    water += 20
    internet += 15
    other += (electricity + 20 + 15) + ((electricity + 20 + 15) * 0.20)

print(f'Electricity: {electricity_price:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {(electricity_price + water + internet + other) / months:.2f} lv')
