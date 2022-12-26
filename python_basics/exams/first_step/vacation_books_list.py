pages = int(input())
page_by_hour = int(input())
days = int(input())
hours = pages / page_by_hour
hours_per_day = round(hours / days)
print(hours_per_day)