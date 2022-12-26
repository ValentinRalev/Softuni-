n = int(input())
n2 = int(input())
operator = input()
result = 0
type = ""
if operator == "+":
    result = n + n2
    if result % 2 == 0:
        type = "even"
    else:
        type = "odd"
    print(f"{n} {operator} {n2} = {result} - {type}")
elif operator == "-":
    result = n - n2
    if result % 2 == 0:
        type = "even"
    else:
        type = "odd"
    print(f"{n} {operator} {n2} = {result} - {type}")
elif operator == "*":
    result = n * n2
    if result % 2 == 0:
        type = "even"
    else:
        type = "odd"
    print(f"{n} {operator} {n2} = {result} - {type}")
elif operator == "/":
    if n2 != 0:
        result = n / n2
        print(f"{n} / {n2} = {result:.2f}")
    else:
        print(f"Cannot divide {n} by zero")
elif operator == "%":
    if n2 != 0:
        result = n % n2
        print(f"{n} % {n2} = {result}")
    else:
        print(f"Cannot divide {n} by zero")



