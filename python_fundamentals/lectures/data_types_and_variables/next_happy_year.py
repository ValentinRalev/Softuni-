year = int(input())
while True:
    year += 1
    current_year = str(year)
    if len(current_year) == len(set(current_year)):
        print(current_year)
        break
