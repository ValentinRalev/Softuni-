movie_budget = float(input())
statist = int(input())
price_uniform = float(input())
decor = movie_budget * 0.10
statist_money = statist * price_uniform
if statist > 150:
    statist_money = statist_money * 0.9
money = decor + statist_money
diff = abs(movie_budget - money)
if money > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
