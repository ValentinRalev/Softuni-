deposit_sum = float(input())
time_deposit = int(input())
annual_percent = float(input())
sum = deposit_sum + time_deposit * ((deposit_sum * annual_percent / 100) / 12)
print(sum)