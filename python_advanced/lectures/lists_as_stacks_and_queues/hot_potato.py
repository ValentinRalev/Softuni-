from collections import deque
names = deque(input().split())
toss = int(input())
while len(names) > 1:
    names.rotate(-toss)
    print(f"Removed {names.pop()}")
print(f"Last is {names.pop()}")
