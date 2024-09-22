PLAYTIME_WORK = 63
PLAYTIME_REST = 127
PLAYTIME_OF_THE_YEAR = 30000

days_for_rest = int(input())

rest_days_time = days_for_rest * PLAYTIME_REST
work_days_time = (365 - days_for_rest) * PLAYTIME_WORK
time_for_tom = rest_days_time + work_days_time
time_in_minutes = abs(time_for_tom - PLAYTIME_OF_THE_YEAR)
H = time_in_minutes // 60
M = time_in_minutes % 60

if time_for_tom > PLAYTIME_OF_THE_YEAR:
    print("Tom will run away")
    print(f"{H} hours and {M} minutes more for play")
elif time_for_tom < PLAYTIME_OF_THE_YEAR:
    print("Tom sleeps well")
    print(f"{H} hours and {M} minutes less for play")
