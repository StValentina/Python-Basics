country = input()
tools = input()

difficulty = 0
performance = 0
points = 0

if tools == 'ribbon':
    if country == 'Russia':
        difficulty = 9.100
        performance = 9.400
        points = difficulty + performance
    elif country == 'Bulgaria':
        difficulty = 9.600
        performance = 9.400
        points = difficulty + performance
    elif country == 'Italy':
        difficulty = 9.200
        performance = 9.500
        points = difficulty + performance

elif tools == 'hoop':
    if country == 'Russia':
        difficulty = 9.300
        performance = 9.800
        points = difficulty + performance
    elif country == 'Bulgaria':
        difficulty = 9.550
        performance = 9.750
        points = difficulty + performance
    elif country == 'Italy':
        difficulty = 9.450
        performance = 9.350
        points = difficulty + performance

elif tools == 'rope':
    if country == 'Russia':
        difficulty = 9.600
        performance = 9.000
        points = difficulty + performance
    elif country == 'Bulgaria':
        difficulty = 9.500
        performance = 9.400
        points = difficulty + performance
    elif country == 'Italy':
        difficulty = 9.700
        performance = 9.150
        points = difficulty + performance


print(f'The team of {country} get {points:.3f} on {tools}.')
print(f'{((20 - points) / 20 * 100):.2f}%')

