rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
cell_bombs = input().split()
for cells in cell_bombs:
    cells = cells.split(",")
    row_index = int(cells[0])
    columns_index = int(cells[1])
    if matrix[row_index][columns_index] > 0:
        bomb_quantity = matrix[row_index][columns_index]
        if row_index == 0:
            if columns_index == 0:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index + 1] > 0:
                    matrix[row_index][columns_index + 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index] > 0:
                    matrix[row_index + 1][columns_index] -= bomb_quantity
                if matrix[row_index + 1][columns_index + 1] > 0:
                    matrix[row_index + 1][columns_index + 1] -= bomb_quantity
            elif columns_index == len(matrix[0]) - 1:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index - 1] > 0:
                    matrix[row_index][columns_index - 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index] > 0:
                    matrix[row_index + 1][columns_index] -= bomb_quantity
                if matrix[row_index + 1][columns_index - 1] > 0:
                    matrix[row_index + 1][columns_index - 1] -= bomb_quantity
            else:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index + 1] > 0:
                    matrix[row_index][columns_index + 1] -= bomb_quantity
                if matrix[row_index][columns_index - 1] > 0:
                    matrix[row_index][columns_index - 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index] > 0:
                    matrix[row_index + 1][columns_index] -= bomb_quantity
                if matrix[row_index + 1][columns_index - 1] > 0:
                    matrix[row_index + 1][columns_index - 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index + 1] > 0:
                    matrix[row_index + 1][columns_index + 1] -= bomb_quantity
        elif row_index == rows - 1:
            if columns_index == 0:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index + 1] > 0:
                    matrix[row_index][columns_index + 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index] > 0:
                    matrix[row_index - 1][columns_index] -= bomb_quantity
                if matrix[row_index - 1][columns_index + 1] > 0:
                    matrix[row_index - 1][columns_index + 1] -= bomb_quantity
            elif columns_index == len(matrix[0]) - 1:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index - 1] > 0:
                    matrix[row_index][columns_index - 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index] > 0:
                    matrix[row_index - 1][columns_index] -= bomb_quantity
                if matrix[row_index - 1][columns_index - 1] > 0:
                    matrix[row_index - 1][columns_index - 1] -= bomb_quantity
            else:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index + 1] > 0:
                    matrix[row_index][columns_index + 1] -= bomb_quantity
                if matrix[row_index][columns_index - 1] > 0:
                    matrix[row_index][columns_index - 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index] > 0:
                    matrix[row_index - 1][columns_index] -= bomb_quantity
                if matrix[row_index - 1][columns_index - 1] > 0:
                    matrix[row_index - 1][columns_index - 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index + 1] > 0:
                    matrix[row_index - 1][columns_index + 1] -= bomb_quantity
        else:
            if columns_index == 0:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index + 1] > 0:
                    matrix[row_index][columns_index + 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index] > 0:
                    matrix[row_index - 1][columns_index] -= bomb_quantity
                if matrix[row_index - 1][columns_index + 1] > 0:
                    matrix[row_index - 1][columns_index + 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index] > 0:
                    matrix[row_index + 1][columns_index] -= bomb_quantity
                if matrix[row_index + 1][columns_index + 1] > 0:
                    matrix[row_index + 1][columns_index + 1] -= bomb_quantity
            elif columns_index == len(matrix[0]) - 1:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index - 1] > 0:
                    matrix[row_index][columns_index - 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index] > 0:
                    matrix[row_index - 1][columns_index] -= bomb_quantity
                if matrix[row_index - 1][columns_index - 1] > 0:
                    matrix[row_index - 1][columns_index - 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index] > 0:
                    matrix[row_index + 1][columns_index] -= bomb_quantity
                if matrix[row_index + 1][columns_index - 1] > 0:
                    matrix[row_index + 1][columns_index - 1] -= bomb_quantity
            else:
                matrix[row_index][columns_index] = 0
                if matrix[row_index][columns_index + 1] > 0:
                    matrix[row_index][columns_index + 1] -= bomb_quantity
                if matrix[row_index][columns_index - 1] > 0:
                    matrix[row_index][columns_index - 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index] > 0:
                    matrix[row_index - 1][columns_index] -= bomb_quantity
                if matrix[row_index - 1][columns_index - 1] > 0:
                    matrix[row_index - 1][columns_index - 1] -= bomb_quantity
                if matrix[row_index - 1][columns_index + 1] > 0:
                    matrix[row_index - 1][columns_index + 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index] > 0:
                    matrix[row_index + 1][columns_index] -= bomb_quantity
                if matrix[row_index + 1][columns_index - 1] > 0:
                    matrix[row_index + 1][columns_index - 1] -= bomb_quantity
                if matrix[row_index + 1][columns_index + 1] > 0:
                    matrix[row_index + 1][columns_index + 1] -= bomb_quantity
count = 0
sum_alive = 0
for nums in matrix:
    for el in nums:
        if el > 0:
            sum_alive += el
            count += 1
print(f"Alive cells: {count}")
print(f"Sum: {sum_alive}")
for r in range(rows):
    print(*matrix[r])
