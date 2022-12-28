import math
height = int(input())
width = int(input())
percent = int(input())
input_line = input()
paint_area = height * width * 4
pain_percent = (100 - percent) / 100
all_area_paint = math.ceil(paint_area * pain_percent)
area = 0
while input_line != "Tired!":
    paint_litres = int(input_line)
    area += paint_litres
    if area >= all_area_paint:
        break





    input_line = input()
diff = abs(all_area_paint - area)
if input_line == "Tired!":
    print(f"{diff} quadratic m left.")
else:
    if area > all_area_paint:
        print(f"All walls are painted and you have {diff} l paint left!")
    elif area == all_area_paint:
        print("All walls are painted! Great job, Pesho!")