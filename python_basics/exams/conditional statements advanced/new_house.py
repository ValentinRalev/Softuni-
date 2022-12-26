type_flowers = input()
number = int(input())
budget = int(input())
sum = 0
if type_flowers == "Roses":
    sum = number * 5
    if number > 80:
        sum = sum * 0.90
elif type_flowers == "Dahlias":
    sum = number * 3.80
    if number > 90:
        sum = sum * 0.85
elif type_flowers == "Tulips":
    sum = number * 2.80
    if number > 80:
        sum = sum * 0.85
elif type_flowers == "Narcissus":
    sum = number * 3
    if number < 120:
        sum = sum * 1.15
elif type_flowers == "Gladiolus":
    sum = number * 2.50
    if number < 80:
        sum = sum * 1.20
diff = abs(budget - sum)
if budget >= sum:
    print(f"Hey, you have a great garden with {number} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")