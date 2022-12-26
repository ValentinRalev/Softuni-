n = int(input())
right_sum = 0
left_sum = 0
for number in range(2 * n):
    current_number = int(input())
    if number < n:
        left_sum += current_number
    else:
        right_sum += current_number
diff = abs(right_sum - left_sum)
if right_sum == left_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")