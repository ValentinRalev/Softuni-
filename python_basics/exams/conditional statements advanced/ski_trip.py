days = int(input())
type = input()
rating = input()
price = 0
if days < 10:
    if type == "room for one person":
        price = (days - 1) * 18
    elif type == "apartment":
        price = ((days - 1) * 25.00) * 0.70
    elif type == "president apartment":
        price = ((days - 1) * 35) * 0.90
elif 10 <= days <= 15:
    if type == "room for one person":
        price = (days - 1) * 18
    elif type == "apartment":
        price = ((days - 1) * 25.00) * 0.65
    elif type == "president apartment":
        price = ((days - 1) * 35) * 0.85
elif days > 15:
    if type == "room for one person":
        price = (days - 1) * 18
    elif type == "apartment":
        price = ((days - 1) * 25.00) * 0.50
    elif type == "president apartment":
        price = ((days - 1) * 35) * 0.80
if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.90
print(f"{price:.2f}")


