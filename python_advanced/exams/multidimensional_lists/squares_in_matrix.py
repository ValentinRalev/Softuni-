rows, columns = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())
count = 0
new_matrix = []
for r in range(rows - 1):
    for c in range(columns - 1):
        temp_square = matrix[r][c], matrix[r][c+1], matrix[r+1][c], matrix[r+1][c+1]
        if len(set(temp_square)) == 1:
            count += 1
print(count)
