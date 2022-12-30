array = [int(x) for x in input().split()]
command = input()
while command != "end":
    command = command.split()
    if command[0] == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        array[first_index], array[second_index] = array[second_index], array[first_index]
    elif command[0] == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        array[first_index] = array[first_index] * array[second_index]
    elif command[0] == "decrease":
        for x in range(len(array)):
            array[x] -= 1
    command = input()
print(", ".join([str(x) for x in array]))
