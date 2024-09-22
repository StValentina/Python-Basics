rent_for_hall = float(input())

statuette_price = rent_for_hall - rent_for_hall * 0.30
catering_price = statuette_price - statuette_price * 0.15
voicing_price = catering_price / 2
total = rent_for_hall + statuette_price + catering_price + voicing_price

print(f'{total:.2f}')

