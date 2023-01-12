rows, columns = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split()])
command = input()
while command != "END":
    command = command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        first_index_r = int(command[1])
        first_index_c = int(command[2])
        second_index_r = int(command[3])
        second_index_c = int(command[4])
        if first_index_r < 0 or first_index_c < 0 or second_index_c < 0 or second_index_r < 0:
            print("Invalid input!")
        elif first_index_r >= len(matrix) or first_index_c >= len(matrix[0]) or second_index_r >= len(matrix) or second_index_c >= len(matrix[0]):
            print("Invalid input!")
        else:
            matrix[first_index_r][first_index_c], matrix[second_index_r][second_index_c] = matrix[second_index_r][second_index_c], matrix[first_index_r][first_index_c]
            for x in range(len(matrix)):
                print(*matrix[x])
    command = input()
