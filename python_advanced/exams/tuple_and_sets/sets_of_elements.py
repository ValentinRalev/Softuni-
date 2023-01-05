first_number, second_number = [int(x) for x in input().split()]
first_set = set()
second_set = set()
for _ in range(first_number):
    number = int(input())
    first_set.add(number)
for _ in range(second_number):
    number_two = int(input())
    second_set.add(number_two)
res = first_set.intersection(second_set)
print("\n".join([str(x) for x in res]))
