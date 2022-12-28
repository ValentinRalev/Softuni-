n_games = int(input())
all_games = 0
game_one = 0
game_two = 0
game_three = 0
game_others = 0
for i in range(1, n_games +1):
    current_game = input()
    all_games += 1

    if current_game == "Hearthstone":
        game_one += 1
    elif current_game == "Fornite":
        game_two += 1
    elif current_game == "Overwatch":
        game_three += 1
    else:
        game_others += 1
game_one_percent = game_one / all_games * 100
game_two_percent = game_two / all_games * 100
game_three_percent = game_three / all_games * 100
game_others_percent = game_others / all_games * 100
print(f"Hearthstone - {game_one_percent:.2f}%")
print(f"Fornite - {game_two_percent:.2f}%")
print(f"Overwatch - {game_three_percent:.2f}%")
print(f"Others - {game_others_percent:.2f}%")