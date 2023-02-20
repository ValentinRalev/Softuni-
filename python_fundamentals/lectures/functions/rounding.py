def rounds(h):
    round_num = []
    for num in (h):
        a = float(num)
        round_num.append(round(a))
    return round_num


number = input().split()
result = rounds(number)
print(result)
