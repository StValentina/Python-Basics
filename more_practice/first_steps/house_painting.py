x = float(input())
y = float(input())
h = float(input())

square_side = (x * x) * 2
door = 1.2 * 2
two_square_side = square_side - door
rectangle_side= (y * x) - (1.5 * 1.5)
two_rectangle_side = rectangle_side * 2
total_side = two_rectangle_side + two_square_side
green_paint_needed = total_side / 3.4

two_rectangle_of_roof = 2 * (x * y)
two_roof_triangle = 2 * (x * h / 2)
total_roof = two_rectangle_of_roof + two_roof_triangle
red_paint_needed = total_roof / 4.3

print('%.2f' % green_paint_needed) # нов синтаксис print(f'{green_paint_needed:.2f}')
print('%.2f' % red_paint_needed) # нов синтаксис print(f'{red_paint_needed:.2f}')