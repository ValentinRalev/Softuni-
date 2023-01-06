n = int(input())
matrix = []
for _ in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)
sum_diagonal = 0
for i in range(n):
    sum_diagonal += matrix[i][i]
print(sum_diagonal)
