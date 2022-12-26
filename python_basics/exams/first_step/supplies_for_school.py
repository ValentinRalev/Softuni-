pen = int(input())
markers = int(input())
detergent = int(input())
percent_dicsount = int(input())
pen_cost = pen * 5.80
markers_cost = markers * 7.20
detergent_cost = detergent * 1.20
all_cost = pen_cost + markers_cost + detergent_cost
total_cost = all_cost - (all_cost * percent_dicsount / 100)
print(f"{total_cost:.2f}")