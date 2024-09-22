client_amount = int(input())

total_price = 0
products = 0
average_sum = 0

for _ in range(client_amount):
    command = input()
    total_price = 0
    products = 0

    while command != 'Finish':
        product_type = command

        if product_type == 'basket':
            price = 1.50
            total_price += price
        elif product_type == 'wreath':
            price = 3.80
            total_price += price
        elif product_type == 'chocolate bunny':
            price = 7
            total_price += price

        products += 1
        command = input()

    if products % 2 == 0:
        total_price *= 0.80

    print(f'You purchased {products} items for {total_price:.2f} leva.')

    average_sum += total_price

print(f'Average bill per client is: {average_sum / client_amount:.2f} leva.')