floors = int(input())
rooms = int(input())
floors_letter = ""
for numbers in range(floors, 0, -1):
    for room in range(rooms):
        if numbers == floors:
            floors_letter = "L"
        elif numbers % 2 == 0:
            floors_letter = "O"
        else:
            floors_letter = "A"
        print(f"{floors_letter}{numbers}{room}" ,end = " ")
    print()





