n_climbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, n_climbers +1):
    current_climbers = int(input())
    if current_climbers <= 5:
        p1 += current_climbers
    elif current_climbers <= 12:
        p2 += current_climbers
    elif current_climbers <= 25:
        p3 += current_climbers
    elif current_climbers <= 40:
        p4 += current_climbers
    else:
        p5 += current_climbers
all_climbers = p1 + p2 + p3 + p4 +p5
p1_percent = p1 / all_climbers * 100
p2_percent = p2 / all_climbers * 100
p3_percent = p3 / all_climbers * 100
p4_percent = p4 / all_climbers * 100
p5_percent = p5 / all_climbers * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")