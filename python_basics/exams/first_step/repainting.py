nylon_needed = int(input())
paint_needed = int(input())
detergent_needed = int(input())
hours_needed = int(input())
all_nylon_cost = (nylon_needed + 2) * 1.50
all_paint_cost = (paint_needed * 1.10) * 14.50
all_detergant_cost = detergent_needed * 5.00
bags = 0.40
all_cost = all_paint_cost + all_nylon_cost + all_detergant_cost + bags
one_hour = all_cost * 0.30
workers_cost = hours_needed * one_hour
full_cost = all_cost + workers_cost
print(full_cost)