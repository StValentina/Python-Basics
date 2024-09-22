first_border = int(input())
second_border = int(input())
third_border = int(input())

for first_n in range(1, first_border + 1):
    for second_n in range(1, second_border + 1):
        for third_n in range(1, third_border + 1):
            if first_n % 2 == 0 and third_n % 2 == 0:
                if second_n == 2 or second_n == 3 or second_n == 5 or second_n == 7:
                    print(first_n, second_n, third_n)
