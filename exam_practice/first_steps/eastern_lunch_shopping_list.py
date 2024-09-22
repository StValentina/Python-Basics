BREAD_PRICE = 3.20
EGGS_PRICE = 4.35
COOKIES_PRICE = 5.40
PAINT_PRICE = 0.15

bread_amount = int(input())
eggs_amount = int(input())
cookies_kilo = int(input())

sum_for_bread = bread_amount * BREAD_PRICE
sum_for_eggs = eggs_amount * EGGS_PRICE
sum_for_cookies = cookies_kilo * COOKIES_PRICE
sum_for_paint =  (eggs_amount * 12) * PAINT_PRICE

total = sum_for_bread + sum_for_eggs + sum_for_cookies + sum_for_paint

print(f'{total:.2f}')
