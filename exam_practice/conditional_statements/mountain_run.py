from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_one_meter = float(input())

time_for_hills = distance_in_meters * seconds_one_meter
delay_of_distance = floor(distance_in_meters / 50)
addition_of_time = delay_of_distance * 30
total_time = floor(time_for_hills + addition_of_time)

if total_time < record_in_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {total_time - record_in_seconds:.2f} seconds slower.')