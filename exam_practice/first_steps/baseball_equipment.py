yearly_fee = int(input())

shoes = yearly_fee - yearly_fee * 0.40
clothes = shoes - shoes * 0.20
ball = clothes / 4
accessories = ball / 5

total = yearly_fee + shoes + clothes + ball + accessories

print(f'{total:.2f}')