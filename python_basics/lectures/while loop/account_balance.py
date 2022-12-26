command = input()
sum = 0
while command != "NoMoreMoney":
    new_command = float(command)

    if new_command < 0:
        print("Invalid operation!")
        break
    sum += new_command
    print(f"Increase: {new_command:.2f}")
    command = input()
print(f"Total: {sum:.2f}")