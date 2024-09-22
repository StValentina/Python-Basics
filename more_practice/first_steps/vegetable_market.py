vegetable_price = float(input())
fruits_price = float(input())
vegetables_kilo_amount = int(input())
fruits_kilo_amount = int(input())

vegetables = vegetable_price * vegetables_kilo_amount
fruits = fruits_price * fruits_kilo_amount

total = (vegetables + fruits) / 1.94

print(f'{total:.2f}')
