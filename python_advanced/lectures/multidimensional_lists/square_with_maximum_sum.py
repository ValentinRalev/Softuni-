rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)
biggest_sum = 0
sum_of_numbers = 0
a = 0
b = 0
c = 0
d = 0
for j in range(columns - 1):
    for r in range(rows - 1):
        sum_of_numbers = matrix[r][j] + matrix[r][j + 1] + matrix[r + 1][j] + matrix[r + 1][j + 1]
        if sum_of_numbers > biggest_sum:
            biggest_sum = sum_of_numbers
            a, b, c, d = matrix[r][j], matrix[r][j + 1], matrix[r + 1][j], matrix[r + 1][j + 1]
print(f"{a} {b}")
print(f"{c} {d}")
print(biggest_sum)