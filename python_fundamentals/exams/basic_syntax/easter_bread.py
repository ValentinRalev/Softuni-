budget = float(input())
flour = float(input())
pack_egg = 0.75 * flour
milk = (flour * 1.25) / 4
cozonac_price = flour + pack_egg + milk
left_bidget = budget
cozonac_count = 0
colored_egg = 0
while left_bidget >= cozonac_price:
    left_bidget -= cozonac_price
    cozonac_count += 1
    colored_egg += 3
    if cozonac_count % 3 == 0:
        colored_egg -= cozonac_count - 2
print(f"You made {cozonac_count} loaves of Easter bread! Now you have {colored_egg} eggs and {left_bidget:.2f}BGN left.")
