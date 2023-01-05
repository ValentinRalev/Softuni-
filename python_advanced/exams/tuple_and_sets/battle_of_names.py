number = int(input())
odd = set()
even = set()
row = 0
for _ in range(number):
    name = input()
    row += 1
    sum_chars = 0
    for char in name:
        sum_chars += ord(char)
    integer_divide = sum_chars // row
    if integer_divide % 2 == 0:
        even.add(integer_divide)
    else:
        odd.add(integer_divide)
if sum(odd) == sum(even):
    res = odd.union(even)
    print(", ".join(str(x) for x in res))
elif sum(odd) > sum(even):
    res = odd.difference(even)
    print(", ".join(str(x) for x in res))
elif sum(odd) < sum(even):
    res = odd.symmetric_difference(even)
    print(", ".join(str(x) for x in res))
