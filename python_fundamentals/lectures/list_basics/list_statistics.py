n_lines = int(input())
positives = []
negatives = []


for i in range(n_lines):
    numbers = int(input())
    if numbers > 0:
        positives.append(numbers)
    else:
        negatives.append(numbers)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}\nSum of negatives: {sum(negatives)}")
