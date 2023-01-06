count_of_row = int(input())
flattened_matrix = []
for _ in range(count_of_row):
    elements = [int(x) for x in input().split(", ")]
    for j in elements:
        flattened_matrix.append(j)
print(flattened_matrix)
