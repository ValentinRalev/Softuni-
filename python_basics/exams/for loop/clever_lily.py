age = int(input())
laundry = float(input())
toy_price = int(input())
sum_even = 0
sum = 0
toys = 0
for i in range(1, age +1):
    if i % 2 == 0:
        sum_even += 10
        sum += sum_even
        sum = sum - 1
    else:
        toys += 1

money_toys = toys * toy_price
money = sum + money_toys
diff = abs(laundry - money)
if laundry <= money:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
