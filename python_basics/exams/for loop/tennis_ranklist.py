from math import floor
number_tournament = int(input())
starting_points = int(input())
points = starting_points
win_tournaments = 0
for i in range(1, number_tournament +1):
    current_position = input()
    if current_position == "W":
        win_tournaments += 1
        points += 2000
    elif current_position == "F":
        points += 1200
    elif current_position == "SF":
        points += 720
average_points = floor((points - starting_points) / number_tournament)
win_percent = win_tournaments / number_tournament * 100
print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")

