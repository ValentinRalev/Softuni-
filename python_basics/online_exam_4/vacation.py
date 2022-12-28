money_needed = float(input())
money = float(input())
spend_save = 0
days = 0
while money < money_needed:
    command = input()
    current_money = float(input())
    days += 1
    if command == "spend":
        spend_save += 1
        if current_money > money:
            current_money = money
        money = money - current_money
    elif command == "save":
        spend_save = 0
        money += current_money
    if spend_save == 5:
        break

if spend_save != 5:
    print(f"You saved the money for {days} days.")
else:
    print("You can't save the money.")
    print(f"{days}")

