number = int(input())
names = set()
for _ in range(number):
    name = input()
    names.add(name)
print("\n".join(names))