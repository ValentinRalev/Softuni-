number = int(input())
matrix_ascii = []
for _ in range(number):
    elements = input()
    new_elements = ""
    for char in elements:
        new_elements += char
    matrix_ascii.append(new_elements)
symbol = input()
never_found = True
for r in range(number):
    for c in range(number):
        if matrix_ascii[r][c] == symbol:
            print(f"({r}, {c})")
            never_found = False
            exit()

if never_found:
    print(f"{symbol} does not occur in the matrix")
