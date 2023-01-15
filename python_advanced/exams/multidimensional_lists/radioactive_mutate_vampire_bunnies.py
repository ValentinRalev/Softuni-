from collections import deque
rows, columns = [int(x) for x in input().split()]
matrix = []
player_position = []
is_dead = False
player_won = False
bunny_position = deque()
for r in range(rows):
    elements = [x for x in input()]
    matrix.append(elements)
    for char in elements:
        if char == "P":
            player_position.append(r)
            player_position.append(elements.index(char))
        elif char == "B":
            bunny_position.append([r, elements.index(char)])

command_line = deque([x for x in input()])
while len(command_line) > 0:
    row = player_position[0]
    column = player_position[1]
    if command_line[0] == "L":
        if column > 0:
            column -= 1
            if matrix[row][column] != "B":
                player_position[1] = column
            else:
                is_dead = True
        else:
            player_won = True
            matrix[row][column] = "."
    elif command_line[0] == "R":
        if column < columns - 1:
            column += 1
            if matrix[row][column] != "B":
                player_position[1] = column
            else:
                is_dead = True
        else:
            player_won = True
            matrix[row][column] = "."
    elif command_line[0] == "U":
        if row > 0:
            row -= 1
            if matrix[row][column] != "B":
                player_position[0] = row
            else:
                is_dead = True
        else:
            player_won = True
            matrix[row][column] = "."
    elif command_line[0] == "D":
        if row < rows - 1:
            row += 1
            if matrix[row][column] != "B":
                player_position[0] = row
            else:
                is_dead = True
        else:
            player_won = True
            matrix[row][column] = "."
    while bunny_position:
        r = bunny_position[0][0]
        c = bunny_position[0][1]

        if r == 0:
            if matrix[r + 1][c] == "P":
                is_dead = True
            matrix[r + 1][c] = "B"
        elif r == rows - 1:
            if matrix[r - 1][c] == "P":
                is_dead = True
            matrix[r - 1][c] = "B"
        else:
            if matrix[r + 1][c] == "P" or matrix[r - 1][c] == "P":
                is_dead = True
            matrix[r + 1][c] = "B"
            matrix[r - 1][c] = "B"
        if c == 0:
            if matrix[r][c + 1] == "P":
                is_dead = True
            matrix[r][c + 1] = "B"
        elif c == columns - 1:
            if matrix[r][c - 1] == "P":
                is_dead = True
            matrix[r][c - 1] = "B"
        else:
            if matrix[r][c + 1] == "P" or matrix[r][c - 1] == "P":
                is_dead = True
            matrix[r][c + 1] = "B"
            matrix[r][c - 1] = "B"
        bunny_position.popleft()
    if player_won:
        break
    if is_dead:
        break
    command_line.popleft()
for k in range(rows):
    print("".join(matrix[k]))
if is_dead:
    print(f"dead: {player_position[0]} {player_position[1]}")
else:
    print(f"won: {player_position[0]} {player_position[1]}")