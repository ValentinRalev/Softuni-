number = int(input())
sum_of_numbers = 0
is_special = False
for n in range(1, number + 1):
    for digit in str(n):
        sum_of_numbers += int(digit)
    if sum_of_numbers == 5 or sum_of_numbers == 7 or sum_of_numbers == 11:
        is_special = True
        print(f"{n} -> {is_special}")
    else:
        is_special = False
        print(f"{n} -> {is_special}")
    sum_of_numbers = 0
