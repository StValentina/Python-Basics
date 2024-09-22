students_amount = int(input())

group_one, group_two, group_three, group_four = 0, 0, 0, 0
students_one, students_two, students_three, students_four = 0, 0, 0, 0

for _ in range(students_amount):
    students_mark = float(input())

    if 5.00 <= students_mark:
        group_one += students_mark
        students_one += 1
    elif 4.00 <= students_mark <= 4.99:
        group_two += students_mark
        students_two += 1
    elif 3.00 <= students_mark <= 3.99:
        group_three += students_mark
        students_three += 1
    elif 2.00 <= students_mark <= 2.99:
        group_four += students_mark
        students_four += 1

print(f'Top students: {(students_one / students_amount) * 100:.2f}%')
print(f'Between 4.00 and 4.99: {(students_two / students_amount) * 100:.2f}%')
print(f'Between 3.00 and 3.99: {(students_three / students_amount) * 100:.2f}%')
print(f'Fail: {(students_four / students_amount) * 100:.2f}%')
print(f'Average: {(group_one + group_two + group_three + group_four) / students_amount:.2f}')

