water_tank = 255
capacity = 0
n = int(input())
for i in range(n):
    litres = int(input())
    capacity += litres
    if capacity > water_tank:
        print("Insufficient capacity!")
        capacity -= litres
print(capacity)
