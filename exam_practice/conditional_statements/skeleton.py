minutes_of_control = float(input())
second_of_control = float(input())
length_in_meters = int(input())
seconds_for_hundred_meters = float(input())

control_in_seconds = int(minutes_of_control * 60 + second_of_control)
time_decrease = length_in_meters / 120
total_time_decrease = time_decrease * 2.5
martin_time = (length_in_meters / 100) * seconds_for_hundred_meters - total_time_decrease

if martin_time <= control_in_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {martin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {martin_time - control_in_seconds:.3f} second slower.')
