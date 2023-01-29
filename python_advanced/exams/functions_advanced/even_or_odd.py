def even_odd(*args):
    result = None
    sign = args[-1]
    if sign == "even":
        result = [int(x) for x in args[:-1] if x % 2 == 0]
    elif sign == "odd":
        result = [int(x) for x in args[:-1] if x % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
