project = input()
package = input()
tickets = int(input())
price = 0
if project == "John Wick":
    if package == "Drink":
        price = 12 * tickets
    elif package == "Popcorn":
        price = 15 * tickets
    elif package == "Menu":
        price = 19 * tickets
elif project == "Star Wars":
    if package == "Drink":
        price = 18 * tickets
    elif package == "Popcorn":
        price = 25 * tickets
    elif package == "Menu":
        price = 30 * tickets
    if tickets >= 4:
        price = price * 0.70
elif project == "Jumanji":
    if package == "Drink":
        price = 9 * tickets
    elif package == "Popcorn":
        price = 11 * tickets
    elif package == "Menu":
        price = 14 * tickets
    if tickets == 2:
        price = price * 0.85
print(f"Your bill is {price:.2f} leva.")


