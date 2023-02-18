def calculate(oper, num1, num2):
    if oper == "multiply":
        return num1 * num2
    elif oper == "divide":
        return int(num1 / num2)
    elif oper == "add":
        return num1 + num2
    elif oper == "subtract":
        return num1 - num2


operator = input()
number_one = int(input())
number_two = int(input())
result = calculate(operator, number_one, number_two)
print(result)
