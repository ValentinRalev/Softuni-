number = int(input())
for row in range(1, number + 1):
    for j in range(1, row + 1):
        print("*", end="")
    print()
for i in range(number - 1, 0, -1):
    for k in range(i, 0, -1):
        print("*", end="")
    print()
