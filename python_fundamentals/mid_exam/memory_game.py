sequence = input().split()
command = input()
moves = 0

is_over = False
while command != "end":
    index_one, index_two = command.split()
    index_one = int(index_one)
    index_two = int(index_two)
    moves += 1
    if index_one == index_two or (0 > index_one or 0 > index_two) or (index_one >= len(sequence) or index_two >= len(sequence)):
        new_element = f"-{moves}a"
        half = len(sequence) // 2
        sequence.insert(half, new_element)
        sequence.insert(half, new_element)
        print("Invalid input! Adding additional elements to the board")
    elif sequence[index_one] == sequence[index_two]:
        element = sequence[index_one]
        if index_one > index_two:
            sequence.pop(index_one)
            sequence.pop(index_two)
        else:
            sequence.pop(index_two)
            sequence.pop(index_one)
        print(f"Congrats! You have found matching elements - {element}!")
    elif sequence[index_one] != sequence[index_two]:
        print("Try again!")
    if len(sequence) == 0:
        is_over = True
        break
    command = input()
if is_over:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(")
    print(" ".join(sequence))
