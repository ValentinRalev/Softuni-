first = int(input())
second = int(input())
third = int(input())
students = int(input())
answers_per_hour = first + second + third
time = 0
while students > 0:
    time += 1
    if time % 4 == 0:
        pass
    else:
        students -= answers_per_hour
print(f"Time needed: {time}h.")
