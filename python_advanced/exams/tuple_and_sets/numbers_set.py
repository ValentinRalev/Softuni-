first_line = set([int(x) for x in input().split()])
second_line = set([int(x) for x in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    numbers_in_command = [int(num) for num in command if num.isdigit()]
    if command[0] == "Add":
        if command[1] == "First":
            for el in numbers_in_command:
                first_line.add(el)
        elif command[1] == "Second":
            for k in numbers_in_command:
                second_line.add(k)
    elif command[0] == "Remove":
        if command[1] == "First":
            for el in numbers_in_command:
                first_line.discard(el)
        elif command[1] == "Second":
            for k in numbers_in_command:
                second_line.discard(k)
    elif command[0] == "Check":
        if first_line.issubset(second_line) or first_line.issuperset(second_line):
            print("True")
        else:
            print("False")
print(", ".join(str(x) for x in sorted(first_line)))
print(", ".join(str(x) for x in sorted(second_line)))
