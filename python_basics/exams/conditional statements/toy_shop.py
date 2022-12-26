price_holiday = float(input())
puzzles = int(input())
speak_toy = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
puzzles_money = puzzles * 2.60
speak_toy_money = speak_toy * 3
bears_money = bears * 4.10
minions_money = minions * 8.20
trucks_money = trucks * 2
all_toys = puzzles + speak_toy + bears + minions + trucks
all_money = puzzles_money + speak_toy_money + bears_money + minions_money + trucks_money
if all_toys >= 50:
    all_money = all_money * 0.75
loan = all_money * 0.1
total_money = all_money - loan
diff = abs(total_money - price_holiday)
if total_money >= price_holiday:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")