starting_point = int(input())
bonus_points = 0
if starting_point <= 100:
    bonus_points = 5
elif 100 < starting_point <= 1000:
    bonus_points = starting_point * 0.2
elif starting_point > 1000:
    bonus_points = starting_point * 0.1
if starting_point % 2 == 0:
    bonus_points += 1
elif starting_point % 10 == 5:
    bonus_points += 2
all_point = starting_point + bonus_points
print(bonus_points)
print(all_point)
