from collections import deque


cups_capacity = deque([int(el) for el in input().split()])
bottles_capacity = [int(el) for el in input().split()]
wasted_water = 0

while cups_capacity:
    current_bottle = bottles_capacity[-1]
    if cups_capacity[0] <= current_bottle:
        wasted_water += (bottles_capacity.pop() - cups_capacity.popleft())
    else:
        cups_capacity[0] -= bottles_capacity.pop()
    if not bottles_capacity:
        break
if bottles_capacity:
    print(f"Bottles: {' '.join([str(el) for el in bottles_capacity])}")
else:
    print(f"Cups: {' '.join([str(el) for el in cups_capacity])}")
print(f"Wasted litters of water: {wasted_water}")