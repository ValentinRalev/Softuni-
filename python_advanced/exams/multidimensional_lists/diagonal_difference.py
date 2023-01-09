number = int(input())
matrix = []
for _ in range(number):
    matrix.append([int(x) for x in input().split()])
primary_sum = 0
secondary_sum = 0
for i in range(number):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][number - 1 - i]
diff = abs(primary_sum - secondary_sum)
print(diff)
