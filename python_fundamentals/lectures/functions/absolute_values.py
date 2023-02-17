number = [float(num) for num in input().split()]
absolute_value = []
for x in number:
    x = abs(x)
    absolute_value.append(x)
print(absolute_value)
