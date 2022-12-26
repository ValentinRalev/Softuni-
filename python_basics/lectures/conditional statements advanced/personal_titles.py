age = float(input())
name = input()
if name == "m":
    if age >= 16:
        print("Mr.")
    elif age < 16:
        print("Master")
elif name == "f":
    if age >= 16:
        print("Ms.")
    elif age < 16:
        print("Miss")
