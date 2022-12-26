height = int(input())
depth = int(input())
width = int(input())
percent = float(input())
area = height * depth * width / 1000
full_area = area - (area * percent / 100)
print(full_area)
