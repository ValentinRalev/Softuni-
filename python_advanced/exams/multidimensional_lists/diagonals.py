rows = int(input())
matrix = []
for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)
sum_primary = 0
primary_diagonal = []
sum_secondary = 0
secondary_diagonal = []
for r in range(rows):
    sum_primary += matrix[r][r]
    primary_diagonal.append(matrix[r][r])
for c in range(rows):
    sum_secondary += matrix[c][rows - c - 1]
    secondary_diagonal.append(matrix[c][rows - c - 1])
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum_secondary}")