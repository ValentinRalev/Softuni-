from math import pi
type = input()
area = 0
if type == "square":
    height = float(input())
    area = height * height

elif type == "rectangle":
    height = float(input())
    width = float(input())
    area = height * width
elif type == "circle":
    radius = float(input())
    area = pi * radius * radius
elif type == "triangle":
    height = float(input())
    width = float(input())
    area = height * width / 2
print(f"{area:.3f}")


