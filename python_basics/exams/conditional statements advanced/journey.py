budget = float(input())
season = input()
destination = ''
accommodation = ''
sum = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        sum = 0.30 * budget
    elif season == "winter":
        accommodation = "Hotel"
        sum = 0.70 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        sum = 0.40 * budget
    elif season == "winter":
        accommodation = "Hotel"
        sum = 0.80 * budget
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    sum = 0.90 * budget
print(f"Somewhere in {destination}")
print(f"{accommodation} - {sum:.2f}")
