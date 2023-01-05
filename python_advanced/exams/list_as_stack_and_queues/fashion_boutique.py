clothes_in_box = [int(x) for x in input().split()]
rack_capacity = int(input())

rack = 1
current_rack = rack_capacity

while clothes_in_box:
    current_clothes = clothes_in_box[-1]
    if current_clothes <= current_rack:
        clothes_in_box.pop()
        current_rack -= current_clothes
    else:
        rack += 1
        current_rack = rack_capacity
print(rack)
