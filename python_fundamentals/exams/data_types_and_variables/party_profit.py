company = int(input())
days = int(input())
coins = 0
for n in range(1, days + 1):
    if n % 10 == 0:
        company -= 2
    if n % 15 == 0:
        company += 5
    coins += 50
    spent_coins = 2 * company
    coins -= spent_coins
    if n % 3 == 0:
        spent_coins = 3 * company
        coins -= spent_coins
    if n % 5 == 0:
        coins += 20 * company
    if n % 3 == 0 and n % 5 == 0:
        spent_coins = 2 * company
        coins -= spent_coins
company_coins = int(coins / company)
print(f"{company} companions received {company_coins} coins each.")
