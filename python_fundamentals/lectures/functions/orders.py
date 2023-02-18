def calculate_price(a, b):
    price = 0
    if a == "coffee":
        price = 1.50 * b
    elif a == "coke":
        price = 1.40 * b
    elif a == "water":
        price = 1.00 * b
    elif a == "snacks":
        price = 2.00 * b
    return f"{price:.2f}"


product = input()
quantity = int(input())
result = calculate_price(product, quantity)
print(result)
