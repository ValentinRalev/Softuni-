rows, columns = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
max_sum = -99999
best_row = 0
best_col = 0
for r in range(rows - 2):
    for c in range(columns - 2):
        temp_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                   matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] + \
                   matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if temp_sum > max_sum:
            max_sum = temp_sum
            best_row = r
            best_col = c
print(f"Sum = {max_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")


