chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())
chicken_cost = chicken_menu * 10.35
fish_cost = fish_menu * 12.40
veggie_cost = veggie_menu * 8.15
all_cost = chicken_cost + fish_cost + veggie_cost
desert = all_cost * 0.2
delivery = 2.50
full_cost = all_cost + desert + delivery
print(f"{full_cost:.2f}")