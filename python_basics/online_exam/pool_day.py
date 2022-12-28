import math
n_people = int(input())
tax_entry = float(input())
price_bed = float(input())
price_umbrella = float(input())
all_tax = tax_entry * n_people
n_umbrella = math.ceil(n_people / 2)
n_bed = math.ceil(n_people * 0.75)
tax_umbrella = price_umbrella * n_umbrella
tax_bed = price_bed * n_bed
all_cost = all_tax + (tax_bed) + (tax_umbrella)
print(f"{all_cost:.2f} lv.")
