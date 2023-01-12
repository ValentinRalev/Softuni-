rows, columns = [int(x) for x in input().split()]
snake = input()
letter = [x for x in snake]
matrix = []
for r in range(rows):
    temp_row = []
    if r % 2 == 0:
        for c in range(columns):
            if len(letter) > 0:
                temp_row.append(letter.pop(0))
            else:
                letter = [x for x in snake]
                temp_row.append(letter.pop(0))
        matrix.append(temp_row)
    else:
        for c in range(columns - 1, -1, -1):
            if len(letter) > 0:
                temp_row.append(letter.pop(0))

            else:
                letter = [x for x in snake]
                temp_row.append(letter.pop(0))
        matrix.append(temp_row[::-1])
for path in range(len(matrix)):
    print("".join(matrix[path]))
