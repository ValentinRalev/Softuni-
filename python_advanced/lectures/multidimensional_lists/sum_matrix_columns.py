count_of_rows, count_of_column = [int(x) for x in input().split(", ")]
matrix_of_numbers = []
for _ in range(count_of_rows):
    elements = [int(x) for x in input().split()]
    matrix_of_numbers.append(elements)
for k in range(count_of_column):
    sum_of_column = 0
    for num in matrix_of_numbers:
        sum_of_column += num[k]
    print(sum_of_column)
