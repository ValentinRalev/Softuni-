budget = float(input())
n_nights = int(input())
price_night = float(input())
percent = int(input())
if n_nights > 7:
    price_night = price_night * 0.95
cost_nights = n_nights * price_night
percent_need = percent * budget / 100
all_cost = cost_nights + percent_need
diff = abs(budget - all_cost)
if budget >= all_cost:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")