numbers = [float(x) for x in input().split()]
occ = {}
for num in numbers:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1

for key, value in occ.items():
    print(f"{key:.1f} - {value} times")
