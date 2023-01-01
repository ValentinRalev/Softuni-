sequence = [int(x) for x in input().split()]
command = input()
count = 0
while command != "End":
    index = int(command)
    if len(sequence) > index >= 0:
        if sequence[index] != -1:
            value = sequence[index]
            sequence.pop(index)
            for x in range(0, len(sequence)):
                if sequence[x] != -1:
                    if sequence[x] > value:
                        sequence[x] -= value
                    else:
                        sequence[x] += value
            sequence.insert(index, value)
            sequence[index] = -1
            count += 1
    command = input()
result = " ".join([str(x) for x in sequence])
print(f"Shot targets: {count} -> {result}")
