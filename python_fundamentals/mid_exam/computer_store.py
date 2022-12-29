command = input()
sum = 0

while command !="special" and command != "regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        sum += price
    command = input()
taxes = 0.20 * sum
total = sum + taxes
if command == "special":
    total = total * 0.90
if total == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {sum:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total:.2f}$")
