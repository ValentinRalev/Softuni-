from collections import deque
robots = input().split(";")
starting_time = input().split(":")
new_time = int(starting_time[0]) * 3600 + int(starting_time[1]) * 60 + int(starting_time[2])
robots_processing = {}
busy_time_robots = {}
for k in robots:
    name, time = k.split("-")
    robots_processing[name] = int(time)
    busy_time_robots[name] = -1
command = input()
line = deque()
while command != "End":
    line.append(command)
    command = input()


def convert_second_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


while line:
    new_time += 1
    item = line.popleft()
    for name, busy_time in busy_time_robots.items():
        if new_time >= busy_time:
            busy_time_robots[name] = new_time + robots_processing[name]
            print(f"{name} - {item} [{convert_second_time(new_time)}]")
            break
    else:
        line.append(item)
