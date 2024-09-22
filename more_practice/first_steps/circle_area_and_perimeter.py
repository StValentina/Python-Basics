from math import pi

r = float(input())

area = pi * r * r
perimeter = 2 * pi * r

print('%.2f' % area) # нов синтаксис print(f'{area:.2f}')
print('%.2f' % perimeter) # нов синтаксис print(f'{perimeter:.2f}')

