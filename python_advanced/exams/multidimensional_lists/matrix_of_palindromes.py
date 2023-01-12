rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    rows_list = []
    for c in range(columns):
        first_last_letter = r + 97
        middle_letter = r + c + 97
        palindrome_letter = chr(first_last_letter) + chr(middle_letter) + chr(first_last_letter)
        rows_list.append(palindrome_letter)
    matrix.append(rows_list)

for x in range(len(matrix)):
    print(*(matrix[x]))
