string_line = input()

parenthes = []

for index in range(len(string_line)):
    if string_line[index] == "(":
        parenthes.append(index)
    if string_line[index] == ")":
        print(string_line[parenthes.pop():index +1])
