tekst = input()
sum = 0
for number in tekst:
    if number == "a":
        sum += 1
    if number == "e":
        sum += 2
    if number == "i":
        sum += 3
    if number == "o":
        sum += 4
    if number == "u":
        sum += 5
print(sum)
