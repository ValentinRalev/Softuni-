income_wish = float(input())
input_line = input()
sum = 0
is_valid = False
while input_line != "Party!":
    is_valid = True
    coctail_price = len(input_line)
    coctails = int(input())
    price = coctail_price * coctails
    if price % 2 != 0:
        price = price * 0.75
    sum += price
    if sum >= income_wish:
        break



    input_line = input()
diff = abs(sum - income_wish)
if is_valid:
    if sum >= income_wish:
        print("Target acquired.")
    else:
        print(f"We need {diff:.2f} leva more.")
else:
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {sum:.2f} leva.")
