number = int(input())
empty_stack = []
for _ in range(number):
    current_number = input().split()
    command = current_number[0]
    if command == "1":
        empty_stack.append(int(current_number[1]))
    elif command == "2" and empty_stack:
        empty_stack.pop()
    elif command == "3" and empty_stack:
        print(max(empty_stack))
    elif command == "4" and empty_stack:
        print(min(empty_stack))
while empty_stack:
    element = empty_stack.pop()
    if empty_stack:
        print(element, end=", ")
    else:
        print(element)
