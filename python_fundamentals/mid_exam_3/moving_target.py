sequence_of_targets = [int(x) for x in input().split()]
command = input()
while not command == "End":
    action, index, number = command.split()
    if action == "Shoot":
        if int(index) < len(sequence_of_targets) and int(index) >= 0:
            sequence_of_targets[int(index)] -= int(number)
            if sequence_of_targets[int(index)] <= 0:
                sequence_of_targets.pop(int(index))
    elif action == "Add":
        if int(index) < len(sequence_of_targets) and int(index) >= 0:
            sequence_of_targets.insert(int(index), int(number))
        else:
            print("Invalid placement!")
    elif action == "Strike":
        left = int(index) - int(number)
        right = int(index) + int(number)
        if right in range(len(sequence_of_targets)) and left in range(len(sequence_of_targets)) and int(index) != 0:
            sequence_of_targets = sequence_of_targets[0:left] + sequence_of_targets[right + 1::]
        else:
            print("Strike missed!")
    command = input()
sequence_of_targets = list(map(str, sequence_of_targets))

print("|".join(sequence_of_targets))
