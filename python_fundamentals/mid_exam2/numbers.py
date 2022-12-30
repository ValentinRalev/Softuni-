sequence = [int(x) for x in input().split()]
average_value = sum(sequence) / len(sequence)
decending_sequence = sorted(sequence, reverse=True)
result = []
count = 0
for x in decending_sequence:
    if x > average_value:
        result.append(x)
        count += 1
    if count == 5:
        break
if count == 0:
    print("No")
else:
    print(" ".join(str(x) for x in result))
