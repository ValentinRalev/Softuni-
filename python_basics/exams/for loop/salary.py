n = int(input())
salary = int(input())
left_salary = salary
for i in range(1, n +1):
    current_web = input()
    if current_web == "Facebook":
        left_salary = left_salary - 150
    elif current_web == "Instagram":
        left_salary = left_salary - 100
    elif current_web == "Reddit":
        left_salary = left_salary - 50
    if left_salary <= 0:
        break

if left_salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{left_salary}")
