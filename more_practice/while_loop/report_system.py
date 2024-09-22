sales_money = int(input())

transaction = 0
payment_count = 0
cash_payment = 0
card_payment = 0
cash_count = 0
card_count = 0

while transaction < sales_money:
    money_payment = input()

    if money_payment == 'End':
        print('Failed to collect required money for charity.')
        break

    payment = int(money_payment)
    payment_count += 1

    if payment_count % 2 != 0:
        if payment > 100:
            print('Error in transaction!')
            continue
        cash_payment += payment
        cash_count += 1
        print('Product sold!')
    else:
        if payment < 10:
            print('Error in transaction!')
            continue
        card_payment += payment
        card_count += 1
        print('Product sold!')

    transaction = cash_payment + card_payment

    if transaction >= sales_money:
        print(f'Average CS: {cash_payment / cash_count:.2f}')
        print(f'Average CC: {card_payment / card_count:.2f}')

