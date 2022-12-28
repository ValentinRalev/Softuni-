movie = input()
hall = input()
ticket = int(input())
price = 0
if movie == "A Star Is Born":
    if hall == "normal":
        price = 7.50 * ticket
    elif hall == "luxury":
        price = 10.50 * ticket
    elif hall == "ultra luxury":
        price = 13.50 * ticket
elif movie == "Bohemian Rhapsody":
    if hall == "normal":
        price = 7.35 * ticket
    elif hall == "luxury":
        price = 9.45 * ticket
    elif hall == "ultra luxury":
        price = 12.75 * ticket
elif movie == "Green Book":
    if hall == "normal":
        price = 8.15 * ticket
    elif hall == "luxury":
        price = 10.25 * ticket
    elif hall == "ultra luxury":
        price = 13.25 * ticket
elif movie == "The Favourite":
    if hall == "normal":
        price = 8.75 * ticket
    elif hall == "luxury":
        price = 11.55 * ticket
    elif hall == "ultra luxury":
        price = 13.95 * ticket
print(f"{movie} -> {price:.2f} lv.")