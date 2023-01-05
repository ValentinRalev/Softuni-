string_line = input()

parentheses_list = []

for index in range(len(string_line)):
    if string_line[index] == "(":
        parentheses_list.append(index)
    if string_line[index] == ")":
        print(string_line[parentheses_list.pop():index + 1])
