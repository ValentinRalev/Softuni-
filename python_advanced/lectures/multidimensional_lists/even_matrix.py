count_of_row = int(input())
matrix_of_numbers = []
for _ in range(count_of_row):
    elements = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix_of_numbers.append(elements)
print(matrix_of_numbers)
