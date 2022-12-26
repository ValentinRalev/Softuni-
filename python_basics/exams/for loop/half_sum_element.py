import sys

n = int(input())
max_num = -sys.maxsize
sum = 0
for number in range(1, n +1):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    sum += current_number
if sum - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (sum - max_num))}")
