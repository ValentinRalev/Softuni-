rent = int(input())
statue = 0.70 * rent
catering = 0.85 * statue
sound = 0.50 * catering
all_cost = rent + statue + catering + sound
print(f"{all_cost:.2f}")
