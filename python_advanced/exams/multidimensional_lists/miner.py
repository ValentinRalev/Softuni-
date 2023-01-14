from collections import deque
number = int(input())
command_line = deque(input().split())
start_position = []
matrix = []
coals = 0
for row in range(number):
    elements = input().split()
    matrix.append(elements)
    if "s" in elements:
        start_position.append(row)
        start_position.append(elements.index("s"))
    for char in elements:
        if char == "c":
            coals += 1
while len(command_line) > 0:
    rows = start_position[0]
    columns = start_position[1]
    if command_line[0] == "left":
        if columns != 0:
            columns -= 1
            if matrix[rows][columns] == "c":
                coals -= 1
                matrix[rows][columns] = "*"
            elif matrix[rows][columns] == "e":
                print(f"Game over! ({rows}, {columns})")
                exit()
            start_position[1] = columns
    elif command_line[0] == "right":
        if columns < number - 1:
            columns += 1
            if matrix[rows][columns] == "c":
                coals -= 1
                matrix[rows][columns] = "*"
            elif matrix[rows][columns] == "e":
                print(f"Game over! ({rows}, {columns})")
                exit()
            start_position[1] = columns
    elif command_line[0] == "up":
        if rows != 0:
            rows -= 1
            if matrix[rows][columns] == "c":
                coals -= 1
                matrix[rows][columns] = "*"
            elif matrix[rows][columns] == "e":
                print(f"Game over! ({rows}, {columns})")
                exit()
            start_position[0] = rows
    elif command_line[0] == "down":
        if rows < number - 1:
            rows += 1
            if matrix[rows][columns] == "c":
                coals -= 1
                matrix[rows][columns] = "*"
            elif matrix[rows][columns] == "e":
                print(f"Game over! ({rows}, {columns})")
                exit()
            start_position[0] = rows
    command_line.popleft()
    if coals == 0:
        print(f"You collected all coal! ({start_position[0]}, {start_position[1]})")
        exit()
if len(command_line) == 0:
    print(f"{coals} pieces of coal left. ({start_position[0]}, {start_position[1]})")
