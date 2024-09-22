finals = input()
tickets_type = input()
tickets_amount = int(input())
photos = input()

tickets_price = 0
total_price = 0

if finals == 'Quarter final':
    if tickets_type == 'Standard':
        tickets_price = 55.50 * tickets_amount
    elif tickets_type == 'Premium':
        tickets_price = 105.20 * tickets_amount
    elif tickets_type == 'VIP':
        tickets_price = 118.90 * tickets_amount

elif finals == 'Semi final':
    if tickets_type == 'Standard':
        tickets_price = 75.88 * tickets_amount
    elif tickets_type == 'Premium':
        tickets_price = 125.22 * tickets_amount
    elif tickets_type == 'VIP':
        tickets_price = 300.40 * tickets_amount

elif finals == 'Final':
    if tickets_type == 'Standard':
        tickets_price = 110.10 * tickets_amount
    elif tickets_type == 'Premium':
        tickets_price = 160.66 * tickets_amount
    elif tickets_type == 'VIP':
        tickets_price = 400 * tickets_amount

if tickets_price > 4000:
    total_price = tickets_price * 0.75
elif tickets_price > 2500:
    total_price = tickets_price * 0.90
else:
    total_price = tickets_price

if photos == 'Y':
    if tickets_price <= 4000:
        total_price = total_price + (tickets_amount * 40)

print(f'{total_price:.2f}')
