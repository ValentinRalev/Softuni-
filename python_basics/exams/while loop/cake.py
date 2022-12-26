width = int(input())
height = int(input())
piece_cake = width * height
command = input()
while command != "STOP":
    current_piece = int(command)
    piece_cake = piece_cake - current_piece
    if piece_cake <= 0:
        break

    command = input()
if piece_cake > 0:
    print(f"{piece_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(piece_cake)} pieces more.")