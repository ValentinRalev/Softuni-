lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
shields_broke = 0
for n in range(1, lost_fights + 1):
    if n % 2 == 0:
        expenses += helmet
    if n % 3 == 0:
        expenses += sword
    if n % 2 == 0 and n % 3 == 0:
        expenses += shield
        shields_broke += 1
    if shields_broke % 2 == 0 and shields_broke > 0:
        shields_broke = 0
        expenses += armor

print(f"Gladiator expenses: {expenses:.2f} aureus")
