command_input = input()
numbers_line = input().split()
Odd = sum([int(x) for x in numbers_line if int(x) % 2 == 1]) * len(numbers_line)
Even = sum([int(x) for x in numbers_line if int(x) % 2 == 0]) * len(numbers_line)
if command_input == "Odd":
    print(Odd)
else:
    print(Even)
