drink = input()
sugar = input()
number = int(input())
price = 0
sum = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.90 * 0.65
        sum = number * price
    elif sugar == "Normal":
        price = 1
        sum = number * price
    elif sugar == "Extra":
        price = 1.20
        sum = number * price
    if number >= 5:
        sum = sum * 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1 * 0.65
        sum = number * price
    elif sugar == "Normal":
        price = 1.20
        sum = number * price
    elif sugar == "Extra":
        price = 1.60
        sum = number * price
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50 * 0.65
        sum = number * price
    elif sugar == "Normal":
        price = 0.60
        sum = number * price
    elif sugar == "Extra":
        price = 0.70
        sum = number * price
if sum > 15:
    sum = sum * 0.80
print(f"You bought {number} cups of {drink} for {sum:.2f} lv.")
