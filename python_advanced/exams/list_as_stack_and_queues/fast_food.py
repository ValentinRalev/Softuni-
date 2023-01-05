from collections import deque

quantity_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]
    if current_order > quantity_food:
        break
    else:
        quantity_food -= current_order
        orders.popleft()
if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")
