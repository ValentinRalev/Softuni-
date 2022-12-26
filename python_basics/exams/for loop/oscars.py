actor_name = input()
academy_points = float(input())
judges = int(input())
starting_points = academy_points

for i in range(1, judges +1):
    current_judge = input()
    points_awarded = float(input())
    starting_points = len(current_judge) * points_awarded / 2 + starting_points
    if starting_points > 1250.5:
        break
if starting_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {starting_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - starting_points):.1f} more!")
