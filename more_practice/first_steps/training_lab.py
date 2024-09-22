import math

width = float(input()) * 100
height = float(input()) * 100

row = (width - 60) / 120
column = (height - 100) / 70
total_amount_of_chair = (row * column) - 3

print(math.trunc(total_amount_of_chair))
