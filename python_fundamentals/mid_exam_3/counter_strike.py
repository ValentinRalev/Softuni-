inital_energy = int(input())
command = input()
won = 0
no_energy = False
while command != "End of battle":
    distance = int(command)
    if inital_energy >= distance:
        inital_energy -= distance
        won += 1
    else:
        no_energy = True
        break
        
    if won % 3 == 0:
        inital_energy += won
    command = input()
if no_energy:
    print(f"Not enough energy! Game ends with {won} won battles and {inital_energy} energy")
else:
    print(f"Won battles: {won}. Energy left: {inital_energy}")
