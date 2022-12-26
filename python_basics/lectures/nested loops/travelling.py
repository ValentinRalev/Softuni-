command = input()
while command != "End":
    current_budget = float(input())
    sum = 0
    while sum < current_budget:
        money = float(input())
        sum += money
    print(f"Going to {command}!")

    command = input()

