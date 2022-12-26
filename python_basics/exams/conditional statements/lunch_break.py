import math
serial_name = input()
time_episode = int(input())
time_rest = int(input())
lunch_time = time_rest / 8
air_time = time_rest / 4
time_needed = time_episode + lunch_time + air_time
diff = abs(time_rest - time_needed)
if time_rest >= time_needed:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(diff)} more minutes.")