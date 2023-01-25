from functools import reduce


def operate(sing, *args):
    if sing == "+":
        return reduce(lambda x, y: x + y, args)
    elif sing == "-":
        return reduce(lambda x, y: x - y, args)
    elif sing == "*":
        return reduce(lambda x, y: x * y, args)
    elif sing == "/":
        return reduce(lambda x, y: x / y, args)


print(operate("*", 3, 4))
