number = int(input())
parking_lot = set()
for _ in range(number):
    action, car = input().split(", ")
    if action == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)
if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")
