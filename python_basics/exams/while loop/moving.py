width = int(input())
height = int(input())
depth = int(input())
area = width * height * depth
command = input()
while command != "Done":
    boxes = int(command)
    area = area - boxes
    if area <= 0:
        break

    command = input()

if area > 0:
    print(f"{area} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(area)} Cubic meters more.")