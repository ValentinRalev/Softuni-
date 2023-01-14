import sys

number = int(input())
second_number = int(input())
max_number = - sys.maxsize
for n in range(number, second_number + 1):
    if n % number == 0:
        if n > max_number:
            max_number = n
print(max_number)
