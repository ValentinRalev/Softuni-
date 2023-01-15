command = input()
coffee = 0
while not command == "END":
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.isupper():
            coffee += 2
        else:
            coffee += 1

    if coffee > 5:
        print("You need extra sleep")
        break
    command = input()
if not coffee > 5:
    print(coffee)
