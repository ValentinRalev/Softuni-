count_of_rows, count_of_columns = [int(x) for x in input().split(", ")]

sum_of_numbers = 0
matrix_of_numbers = []
for _ in range(count_of_rows):
    elements = [int(x) for x in input().split(", ")]
    matrix_of_numbers.append(elements)
    sum_of_numbers += sum(elements)
print(sum_of_numbers)
print(matrix_of_numbers)
