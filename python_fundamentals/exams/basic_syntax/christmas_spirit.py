quantity = int(input())
days = int(input())
ornament = 2
tree_skirt = 5
garlands = 3
light = 15

spirit = 0
cost = 0
for days_left in range(1, days +1):
    if days_left % 11 == 0:
        quantity += 2
    if days_left % 2 == 0:
        cost += 2 * quantity
        spirit += 5
    if days_left % 3 == 0:
        cost += (5 + 3) * quantity
        spirit += 13
    if days_left % 5 == 0:
        cost += 15 * quantity
        spirit += 17
    if days_left % 3 == 0 and days_left % 5 == 0:
        spirit += 30
    if days_left % 10 == 0:
        spirit -= 20
        cost += 5 + 3 + 15

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
