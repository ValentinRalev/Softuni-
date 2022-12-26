budget = float(input())
videocard = int(input())
processors = int(input())
ram = int(input())
price_video = videocard * 250
price_processors = price_video * 0.35 * processors
price_ram = price_video * 0.1 * ram
price = price_video + price_ram + price_processors
if videocard > processors:
    price = 0.85 * price
diff = abs(budget - price)
if budget >= price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
