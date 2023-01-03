from collections import deque

number_of_pumps = int(input())
petrol_pumps = deque()
for _ in range(number_of_pumps):
    current_pumps = [int(x) for x in input().split()]
    petrol_pumps.append(current_pumps)
for attempts in range(number_of_pumps):
    tank = 0
    failed = False
    for amount, distance in petrol_pumps:
        tank += amount
        if tank < distance:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(attempts)
        break
