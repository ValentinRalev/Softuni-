line_of_parentheses = input()
opening_brackets = []
failed = False
for char in line_of_parentheses:
    if char in "({[":
        opening_brackets.append(char)
    else:
        if opening_brackets:
            last_element = opening_brackets[-1]
            if not last_element + char in "(){}[]":
                failed = True
                break
            else:
                opening_brackets.pop()
        else:
            failed = True
            break
if failed:
    print("NO")
else:
    print("YES")
