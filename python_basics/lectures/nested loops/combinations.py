n = int(input())
counter = 0
for number in range(0, n +1):
    for second_number in range(0, n +1):
        for third_number in range(0, n +1):
            if number + second_number + third_number == n:
                counter += 1


print(counter)