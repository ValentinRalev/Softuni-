city = input()
package = input()
vip_discount = input()
days = int(input())
price = 0
sum = 0
is_valid = False
if city == "Bansko" or city == "Borovets":
    if package == "withEquipment":
        is_valid = True
        price = 100
        if vip_discount == "yes":
            price = 100 * 0.90
    elif package == "noEquipment":
        is_valid = True
        price = 80
        if vip_discount == "yes":
            price = 80 * 0.95
elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        is_valid = True
        price = 130
        if vip_discount == "yes":
            price = 130 * 0.88
    elif package == "noBreakfast":
        is_valid = True
        price = 100
        if vip_discount == "yes":
            price = 100 * 0.93
if days > 7:
    sum = (days - 1) * price
else:
    sum = days * price
if days < 1:
    print("Days must be positive number!")
elif days > 1:
    if is_valid:
        print(f"The price is {sum:.2f}lv! Have a nice time!")
    else:
        print("Invalid input!")

