hours = int(input())
minutes = int(input())
new_hours = hours * 60
time = new_hours + minutes + 15
new_hour = time // 60
new_minute = time % 60
if new_hour > 23:
    new_hour = 0
if new_minute < 10:
    print(f"{new_hour}:0{new_minute}")
else:
    print(f"{new_hour}:{new_minute}")