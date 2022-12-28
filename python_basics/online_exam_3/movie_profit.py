movie = input()
days = int(input())
tickets = int(input())
price = float(input())
percent = int(input())
money = tickets * price * days
cost = money - (money * percent) / 100
print(f"The profit from the movie {movie} is {cost:.2f} lv.")
