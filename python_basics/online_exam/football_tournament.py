football_team = input()
games = int(input())
points = 0
win = 0
lost = 0
draw = 0
total_games = 0
for i in range(1, games +1):
    total_games += 1
    result = input()
    if result == "W":
        win += 1
        points += 3
    elif result == "D":
        draw += 1
        points += 1
    elif result == "L":
        lost += 1


if games == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    win_rate = win / total_games * 100
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {win}")
    print(f"## D: {draw}")
    print(f"## L: {lost}")
    print(f"Win rate: {win_rate:.2f}%")

