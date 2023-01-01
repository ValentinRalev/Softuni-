from collections import  deque
quantity = int(input())
name = input()
water_people = deque()
while name != "Start":
    water_people.append(name)
    name = input()
command = input()
while command != "End":
    command = command.split()
    if command[0] == "refill":
        litres = int(command[1])
        quantity += litres
    else:
        litres = int(command[0])
        if quantity >= litres:
            quantity -= litres
            print(f"{water_people.popleft()} got water")
        else:
            print(f"{water_people.popleft()} must wait")
    command = input()
print(f"{quantity} liters left")